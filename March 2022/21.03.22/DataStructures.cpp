#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

string name, phoneNum;

void ContactAdd();
void ContactSearch();
void exitContact();
bool digitCheck(string);
bool numCheck(string);

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
            break;
        case 3:
            exitContact();
            break;
        default:
            getch();
            main();
    }
    return 0;
}

void exitContact()
{
    cout << "Program end.";
    exit(1);
}

void ContactAdd()
{
    ofstream phone("database.txt", ios::app);
    cout << "Enter name: ";
    cin >> name;
    cout << "Enter phone numer (10 digits): ";
    cin >> phoneNum;

    if (digitCheck(phoneNum) == true)
    {
        if(numCheck(phoneNum) == true)
        {
            if(phone.is_open())
            {
                phone << name << " " << phoneNum << endl;
                cout << "\nSaved.";
            }
            else
            {
                cout << "\n Error";
            }
        }
        else
        {
            cout << "\nMust contain numbers only.";
        }
    }
    else
    {
        cout << "\nMust contain 10 digits.";
    }
    phone.close();
}

void ContactSearch()
{
    bool found = false;
    ifstream myfile("database.txt");
    string keyword;
    cout << "\n\tEnter Name To Search : ";
    cin >> keyword;
    while(myfile >> name >> phoneNum)
    {
        if(keyword == name)
        {
            cout << "\n\n\n\t\tDetails";
            cout << "\nName : " << name;
            cout << "\n\tPhone Number : " << phoneNum;
            found = true;
            break;
        }
    }
    if(found == false)
    cout << "\n\tNone exist";
}

bool digitCheck(string x)
{
    if(x.length() == 10)
    return true;
    else
    return false;
}

bool numCheck(string x)
{
    bool check = true;

    for(int i=0; i < x.length(); i++)
    {
        if(!(int(x[i]) >= 48 && int(x[i]) <= 57))
        {
            check = false;
            break;
        }
    }

    if(check == true)
    return true;
    if(check == false)
    return false;
}
