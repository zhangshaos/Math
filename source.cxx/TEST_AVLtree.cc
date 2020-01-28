#include <AVLtree.hpp>
using namespace std;

int main() {
    cout << "测试Insert函数" << endl;
    zxm::AvlTree<int> avltree;
    for (int i = 0; i < 10; ++i) {
        avltree.Insert(std::move(i));
    }
    avltree.Print();
    auto cpy = avltree;
    cout << "\n测试Remove函数" << endl;
    for (int i = 0; i < 10; i++) {
        avltree.Remove(std::move(i));
    }
    avltree.Print();
    cout << "\n测试复制Copy函数" << endl;
    cpy.Print();
    cout << "\n测试移动Copy函数" << endl;
    auto mv = std::move(cpy);
    mv.Print();
    cout << "\n被移动后的函数\n";
    cpy.Print();
    cout << "\n测试极值" << endl;
    cout << "Min:" << mv.GetMin()
        << "Max:" << mv.GetMax();
    
    return 0;
}