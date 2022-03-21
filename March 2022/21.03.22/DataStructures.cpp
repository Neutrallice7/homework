#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

void ContactAdd();
void ContactSearch();
void exitContact();
bool digitCheck();
bool numCheck();

int main()
{
    short int choice;
    cout << "Contact Management.";
    cout << "\n1. Add Contact \n2. Search Contact\n3. Exit";
    cin >> choice;

    switch(choice)
    {
        case 1:
            ContactAdd();
            break;
        case 2:
            ContactSearch();
        case 3:
            exitContact();
            break;
        default:
            getch();
            main();
    }
    return 0;
};

void exitContact()
{
    cout << "Program end.";
    exit(1);
}

void ContactAdd()
{
    
}
