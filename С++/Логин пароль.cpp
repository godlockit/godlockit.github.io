#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct User {
    string username;
    string password;
};

void registerUser(const string& username, const string& password) {
    ofstream usersFile("users.txt", ios::app);
    if (usersFile.is_open()) {
        usersFile << username << " " << password << endl;
        usersFile.close();
        cout << "User registered successfully!" << endl;
    } else {
        cerr << "Unable to open file for writing!" << endl;
    }
}

bool loginUser(const string& username, const string& password) {
    ifstream usersFile("users.txt");
    if (usersFile.is_open()) {
        string storedUsername, storedPassword;
        while (usersFile >> storedUsername >> storedPassword) {
            if (storedUsername == username && storedPassword == password) {
                usersFile.close();
                return true;
            }
        }
        usersFile.close();
    }
    return false;
}

int main() {
    string username, password;
    
    // Регистрация пользователя
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    
    registerUser(username, password);
    
    // Вход пользователя
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    
    if (loginUser(username, password)) {
        cout << "Login successful!" << endl;
    } else {
        cout << "Login failed. User not found or incorrect password." << endl;
    }
    
    return 0;
}
