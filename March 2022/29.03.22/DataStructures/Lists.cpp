#include <iostream>
using namespace std;

struct Node{
    int currNode;
    Node* next;
};

void reverse(Node* pointer){
    if (pointer != nullptr ){
        reverse(pointer->next);
        cout << pointer ->currNode << endl;
    }
}

int main(){
    Node* head;
    Node* node1 = new Node;
    Node* node2 = new Node;
    Node* node3 = new Node;

    node1->currNode = 1;
    node2->currNode = 2;
    node3->currNode = 3;

    head = node1;
    node1 -> next = node2;
    node2 -> next = node3;
    node3 -> next = nullptr;

    reverse(head);
}