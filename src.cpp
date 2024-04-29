#include <iostream> // Bibliothek fuer IO
#include <string>
#include <cmath>
using namespace std;

//game constants

//player creation an initialization
class players {
public:
	string name;
	int life_cnt;
	int cmd_dmg;
	int toxic_cnt;
	bool out_of_cards;
};

//init all players
players player1;
players player2;
players player3;
players player4;
players player5;

player1.life_cnt = lifecount_start;
player1.cmd_dmg = 0;
player1.toxic_cnt = 0;
player1.out_of_cards = false;

player2.life_cnt = lifecount_start;
player2.cmd_dmg = 0;
player2.toxic_cnt = 0;
player2.out_of_cards = false;

player3.life_cnt = lifecount_start;
player3.cmd_dmg = 0;
player3.toxic_cnt = 0;
player3.out_of_cards = false;

player4.life_cnt = lifecount_start;
player4.cmd_dmg = 0;
player4.toxic_cnt = 0;
player4.out_of_cards = false;

player5.life_cnt = lifecount_start;
player5.cmd_dmg = 0;
player5.toxic_cnt = 0;
player5.out_of_cards = false;

//game
const int cmd_dmg_max = 21;
const int toxic_cnt_max = 10;
const int min_players = 2;
const int max_players = 5;

//inits
int player_cnt = 0;
int a = 0;
int lifecount_start = 40;
int rounds_cnt = 0;


void main() {
	//entering the number of players
	cout << "Minimum number of players: " + min_players << endl;
	cout << "Maximum number of players: " + max_players << endl;
	cout << "How many players are there?";
	cin >> player_cnt;

	//entering the names of each player

	naming_players(player_cnt);

	//entering the number of rounds

	cout << "How many games do you want to play?" << endl;
	cin >> rounds_cnt;

	// declaring the starter by random choice

	int starter = rand() % player_cnt + min_players;

	// start of game

	// the game

	// end of game

	// saving the score

	// rounds, points

	// effects like toxic or raditation

	// display functions

	// button functions


	cout << "this code does nothing yet";
}

void naming_players(a) {
	cout << "Enter the name of player 1: ";
	cin >> player1.name;

	switch (a) {
		case(5):
			cout << "Enter the name of player 2: ";
			cin >> player2.name;
			cout << "Enter the name of player 3: ";
			cin >> player3.name;
			cout << "Enter the name of player 4: ";
			cin >> player4.name;
			cout << "Enter the name of player 5: ";
			cin >> player5.name;
		case(4):
			cout << "Enter the name of player 2: ";
			cin >> player2.name;
			cout << "Enter the name of player 3: ";
			cin >> player3.name;
			cout << "Enter the name of player 4: ";
			cin >> player4.name;
		case(3):
			cout << "Enter the name of player 2: ";
			cin >> player2.name;
			cout << "Enter the name of player 3: ";
			cin >> player3.name;
		case(2):
			cout << "Enter the name of player 2: ";
			cin >> player2.name;
	}
		
}