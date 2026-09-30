#include <iostream>
#include <queue>
#include <set>
using namespace std;

struct State
{
    int x, y;
};

void waterJug(int a, int b, int target)
{
    queue<State> q;
    set<pair<int, int>> visited;

    q.push({0, 0});
    visited.insert({0, 0});

    while (!q.empty())
    {
        State current = q.front();
        q.pop();

        int x = current.x;
        int y = current.y;

        cout << "(" << x << ", " << y << ")" << endl;

        if (x == target || y == target)
        {
            cout << "Target achieved!" << endl;
            return;
        }

        // Fill jug A
        if (!visited.count({a, y}))
        {
            visited.insert({a, y});
            q.push({a, y});
        }

        // Fill jug B
        if (!visited.count({x, b}))
        {
            visited.insert({x, b});
            q.push({x, b});
        }

        // Empty jug A
        if (!visited.count({0, y}))
        {
            visited.insert({0, y});
            q.push({0, y});
        }

        // Empty jug B
        if (!visited.count({x, 0}))
        {
            visited.insert({x, 0});
            q.push({x, 0});
        }

        // Pour A into B
        int amount = min(x, b - y);
        int newX = x - amount;
        int newY = y + amount;

        if (!visited.count({newX, newY}))
        {
            visited.insert({newX, newY});
            q.push({newX, newY});
        }

        // Pour B into A
        amount = min(y, a - x);
        newX = x + amount;
        newY = y - amount;

        if (!visited.count({newX, newY}))
        {
            visited.insert({newX, newY});
            q.push({newX, newY});
        }
    }

    cout << "Target cannot be achieved." << endl;
}

int main()
{
    int jugA = 4;
    int jugB = 3;
    int target = 2;

    waterJug(jugA, jugB, target);

    return 0;
}