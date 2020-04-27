#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include <time.h>
using namespace std;
int checkbulls(int ref,int n) {
    int bulls = 0;
    string q = to_string(ref);
    string p = to_string(n);
    for(int i = 0;i < 4;i++) {
        if(p.at(i) == q.at(i)) bulls++;
    }
    return bulls;
}
int checkcows(int ref,int n) {
    int found = 0;
    int cows = 0;
    string q = to_string(ref);
    string p = to_string(n);
    for(int i = 0;i < 4;i++) {
        for(int j = 0;j < 4;j++) {
            if(q.at(i) == p.at(j)) found = 1;
        }
        if(found == 1) {
            cows++;
            found = 0;
        }
    }
    int h = cows - checkbulls(ref,n);
    return h;
}
void ask(int &bulls,int &cows) {
    cin >> bulls >> cows;
	return;
}
void display(int* a) {
	for(int i = 0;i < 4;i++) {
		cout << a[i];
	}
	cout << endl;
	return;
}
struct node{
    int data;
    node* next;
    node* prev;
};
struct list{
    node* head;
    node* tail;
    list() {
        head = tail = NULL;
    }
    int size() {
        if(head == NULL) return 0;
        else {
            int i = 1;
            node*temp = head;
            while(temp->next != NULL) {
                i++;
                temp = temp->next;
            }
            return i;
        }
    }
    void insert(int a) {
        node* temp = new node;
        temp->data = a;
        temp->next = NULL;
        temp->prev = NULL;
        if(head == NULL) {
            head = temp;
            tail = temp;
            head->next = tail;
            head->prev = NULL;
            tail->prev = head;
            tail->next = NULL;
        }
        else {
            temp->prev = tail;
            temp->next = NULL;
            tail->next = temp;
            tail = tail->next;
        }
    }
    void display() {
        node *temp = head;
        while(temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
    int printRandom() {
        if (head == NULL) {}
            srand(time(NULL));
            int result = head->data;
            node *current = head;
            for (int n = 2;current != NULL;n++)  {
                if (rand() % n == 0)
                result = current->data;
                current = current->next;
            }
        return result;
    }
    void remove(int s) {
        if(head == NULL) {}
        else if(head->next == NULL) {
            if(head->data == s) {
                head = NULL;
            }
        }
        else if(head->next->next == NULL) {
            int del = 0;
            if(head->data == s) {
                del++;
                head = head->next;
                head->prev = NULL;
                head->next = NULL;
            }
            else if((tail->data == s) && (del <= 0)) {
                tail = tail->prev;
                tail->next = NULL;
                tail->prev = NULL;
            }
        }
        else {
            int del = 0;
            node *temp = head->next;
            if(head->data == s) {
                head = head->next;
                head->prev = NULL;
                del++;
            }
            else if((tail->data == s) && (del <= 0)) {
                tail = tail->prev;
                tail->next = NULL;
                del++;
            }
            else if(del <= 0) {
                while((temp->next != NULL) && (temp->data != s)) {
                    temp = temp->next;
                }
                if(temp == tail) {
                    del++;
                }
                else if((temp->data == s) && (del <= 0)) {
                    temp->prev->next = temp->next;
                    temp->next->prev = temp->prev;
                }
            }
        }
    }
};
int main() {
    list lkn;
    int j = 1023;
    string f;
    for(int i = 0;i < 8854;i++) {
        f = to_string(j);
        if(f.at(0) != f.at(1) and f.at(0) != f.at(2)) {
            if(f.at(0) != f.at(3) and f.at(1) != f.at(2)) {
                if(f.at(1) != f.at(3) and f.at(2) != f.at(3)) lkn.insert(j);
            }
        } 
        j++;
    }
    int bulls = 0;
    int cows = 0;
    int our_sec = lkn.printRandom();
    cout << our_sec << endl;
    int opp_guess = 1111;
    int read = 0;
    cin >> read;
    int n = lkn.head->data;
    node *temp;
    if(read == 1) {
        while(bulls != 4) {
            temp = lkn.head;
            temp->data = lkn.head->data;
            temp->next = lkn.head->next;
            temp->prev = lkn.head->prev;
            cout << n << endl;
            ask(bulls,cows);
            for(int i = 0;i < 4536;i++) {
                if(checkbulls(temp->data,n) != bulls or checkcows(temp->data,n) != cows) {
                    lkn.remove(temp->data);
                    if(temp->next != NULL) temp = temp->next;
                }
                else if(checkbulls(temp->data,n) == bulls && checkcows(temp->data,n) == cows && temp->next != NULL) temp = temp->next;
            }
            cin >> opp_guess;
            cout << checkbulls(our_sec,opp_guess) << endl << checkcows(our_sec,opp_guess) << endl;
            n = lkn.printRandom();
        }
    }
    if(read == 0) {
        while(bulls != 4) {
                cin >> opp_guess;
                cout << checkbulls(our_sec,opp_guess) << endl << checkcows(our_sec,opp_guess) << endl;
            temp = lkn.head;
            temp->data = lkn.head->data;
            temp->next = lkn.head->next;
            temp->prev = lkn.head->prev;
            cout << n << endl;
            ask(bulls,cows);
            for(int i = 0;i < 4536;i++) {
                if(checkbulls(temp->data,n) != bulls or checkcows(temp->data,n) != cows) {
                    lkn.remove(temp->data);
                    if(temp->next != NULL) temp = temp->next;
                }
                else if(checkbulls(temp->data,n) == bulls && checkcows(temp->data,n) == cows && temp->next != NULL) temp = temp->next;
            }
            n = lkn.printRandom();
        }
    }
}