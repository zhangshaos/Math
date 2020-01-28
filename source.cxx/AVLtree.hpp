// brief: AVL tree implement...
// author: Xingming Zhang
// time: 20-1-28

#ifndef __ZXM_AVLTREE_HPP__
#define __ZXM_ALVTREE_HPP__

#include <cmath>
#include <cassert>
#include <iostream>

namespace zxm {

// imblanced value for AVL tree
static constexpr int k_allowed_imbalance = 1;

// AVL tree, don't support the same nodes.
template <typename Elem>
class AvlTree {
private:
    struct AvlNode {
        Elem element;
        AvlNode *left, *right;
        int height;

        AvlNode(Elem && elem, AvlNode *lft, AvlNode *rght, int h = 0)
            : element{ elem }, left{ lft }, right{ rght }, height{ h } {}
        AvlNode(const AvlNode &) = default;
        AvlNode(AvlNode && other) {
            element = other.element;
            left = other.left;
            other.left = nullptr;
            right = other.right;
            other.right = nullptr;
            height = other.height;
            other.height = 0;
        }
        AvlNode& operator=(const AvlNode &) = default;
        AvlNode& operator=(AvlNode && other) {
            element = other.element;
            left = other.left;
            other.left = nullptr;
            right = other.right;
            other.right = nullptr;
            height = other.height;
            other.height = 0;
            return *this;
        }
        ~AvlNode() {
            // do nothing!
            // let tree determine whether delete node recursively
            // rather than node.
        }
    };
    // get height of a tree, nullptr return 0, leaf node return 1
    static int GetHeight(const AvlNode *p) {
        return p == nullptr ? 0 : p->height;
    }
    // rotate @p and its left child
    static void RotateWithLeft(AvlNode* &p) {
        AvlNode *root = p->left;
        p->left = root->right;
        root->right = p;
        p = root;
        p->right->height = std::max(GetHeight(p->right->left),
                            GetHeight(p->right->right)) + 1;
        p->height = std::max(GetHeight(p->left), GetHeight(p->right)) + 1;
    }
    static void RotateWithRight(AvlNode* &p) {
        AvlNode *root = p->right;
        p->right = root->left;
        root->left = p;
        p = root;
        p->left->height = std::max(GetHeight(p->left->left),
                            GetHeight(p->left->right)) + 1;
        p->height = std::max(GetHeight(p->left), GetHeight(p->right)) + 1;
    }
    // rotate @p, its left child and its left-right grand child 
    static void DoubleRotWithLeft(AvlNode* &p) {
        RotateWithRight(p->left);
        RotateWithLeft(p);
    }
    static void DoubleRotWithRight(AvlNode* &p) {
        RotateWithLeft(p->right);
        RotateWithRight(p);
    }
    // make balance in a position of @p.
    static void MakeBalance(AvlNode* &p) {
        if (p == nullptr) {
            return;
        } else if (GetHeight(p->left) - GetHeight(p->right) >
                    k_allowed_imbalance) {
            // if left tree is imbalanced
            if (GetHeight(p->left->left) >= GetHeight(p->left->right)) {
                // if "outside" case, just rotate once
                RotateWithLeft(p);
            } else {
                // "inside" case, rotate twice
                DoubleRotWithLeft(p);
            }
        } else if (GetHeight(p->right) - GetHeight(p->left) >
                    k_allowed_imbalance) {
            // if right tree is imbalanced
            if (GetHeight(p->right->right) >= GetHeight(p->right->left)) {
                // if "outside" case
                RotateWithRight(p);
            } else {
                // "inside" case
                DoubleRotWithRight(p);
            }
        } else {
            // do nothing
        }
        p->height = std::max(GetHeight(p->left), GetHeight(p->right)) + 1;
    }
    // insert a element in a position of @p to node.
    // if @value is existing, return false, else return true
    static bool Insert(Elem && value, AvlNode* &p) {
        bool is_inserted = true;
        if (p == nullptr) {
            p = new AvlNode{ std::move(value), nullptr, nullptr, 1 };
        } else if (value < p->element) {
            is_inserted = Insert(std::move(value), p->left);
        } else if (value > p->element) {
            is_inserted = Insert(std::move(value), p->right);
        } else {
            // if value == @p->value
            is_inserted = false;
        }
        MakeBalance(p); // post-order modify @p's height
        return is_inserted;
    }
    // find minimum of subtree @p
    // if @p is nullptr, return nullptr
    static AvlNode* FindMin(AvlNode *p) {
        if (nullptr == p->left) {
            return p;
        } else {
            return FindMin(p->left);
        }
    }
    // find maximum of subtree @p
    // if @p is nullptr, return nullptr
    static AvlNode* FindMax(AvlNode *p) {
        if (nullptr == p->right) {
            return p;
        } else {
            return FindMax(p->right);
        }
    }
    // remove a item from a subtree
    // if value doesn't exists, return false, else return true
    static bool Remove(const Elem &value, AvlNode* &p) {
        bool is_existing = true;
        if (p == nullptr) {
            return false;
        }
        if (value < p->element) {
            is_existing = Remove(value, p->left);
        } else if (value > p->element) {
            is_existing = Remove(value, p->right);
        } else {
            // find @value
            is_existing = true;
            if (p->left && p->right) {
                // if @p have both left and right subtree
                static int flip = 0;
                // we have to choose which element to replace the root,
                // when delete root from a subtree with two child.
                // we use @filp to choose max of left-tree and min of right tree for replacement.
                if (flip % 2 == 0) {
                    p->element = FindMax(p->left)->element;
                    Remove(p->element, p->left);
                } else {
                    p->element = FindMin(p->right)->element;
                    Remove(p->element, p->right);
                }
            } else {
                AvlNode *old = p;
                p = p->left != nullptr ? p->left : p->right;
                delete old;
            }
        }

        MakeBalance(p); // post-order modify height
        return is_existing;
    }
    // release all nodes of subtree @p and make @p be nullptr
    static void MakeEmpty(AvlNode* &p) {
        if (p == nullptr) {
            return;
        } else {
            MakeEmpty(p->left);
            MakeEmpty(p->right);
            delete p; // post-order
            p = nullptr;
        }
    }
    // return a copy of tree @src
    // you must call MakeEmpty(retuen-value) by yourself at end!
    static AvlNode* Clone(const AvlNode * src) {
        if (src == nullptr) {
            return nullptr;
        } else {
            auto elem = src->element;
            return new AvlNode{ std::move(elem),
                    Clone(src->left), Clone(src->right), GetHeight(src) };
        }
    }
    // print tree's info with out stream
    // you must overwrite "operator<<(Elem)" before!
    static void Print(const AvlNode * p, int indent = 0,
                    std::ostream & out = std::cout) {
        // pre-order
        if (p) {
            out << '\n';
            for (int i = 0; i < indent; ++i) {
                out << ' ';
            }
            out << p->element;
            Print(p->left, indent + 1, out);
            Print(p->right, indent + 1, out);
        } else {
            out << '\n';
            for (int i = 0; i < indent; ++i) {
                out << ' ';
            }
            out << "NULL";
        }
    }

public:
    // insert a element
    // if @value already exists, return false, else return true
    bool Insert(Elem && value) {
        return Insert(std::move(value), root);
    }
    bool Remove(const Elem & value) {
        return Remove(value, root);
    }
    void Print(std::ostream & out = std::cout) {
        Print(root, 0, out);
    }
    const Elem & GetMin() {
        return FindMin(root)->element;
    }
    const Elem & GetMax() {
        return FindMax(root)->element;
    }

    AvlTree() : root{nullptr} {}
    AvlTree(const AvlTree & other) {
        root = Clone(other.root);
    }
    AvlTree(AvlTree && other) {
        root = other.root;
        other.root = nullptr;
    }
    AvlTree& operator=(const AvlTree & other) {
        AvlTree cpy = other;
        std::swap(cpy.root, root);
    }
    AvlTree& operator=(AvlTree && other) {
        root = other.root;
        other.root = nullptr;
    }
    ~AvlTree() {
        MakeEmpty(root);
    }

private:
    AvlNode *root;
};

}
#endif