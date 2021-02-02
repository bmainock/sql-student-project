import json
import multiprocessing

# WINSIZE = (Cell.w * 41, Cell.h * 41)


def main():
    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    f = open('state_data.json')
    data = json.load(f)
    for states in data['states']:
        print(states)

    print(type(data))
    print(len(data['states']))

    while True:
        print("what would you like to know\n")
        search = input()



        # returns names of states
        if search in "names":
            for state in data['states']:
                print(state['stateNames'])

        if "nam" in search:
            print("did you mean names? (y/n)")
            search = input()
            if search == 'yes' or 'y':
                for state in data['states']:
                    print(state['stateNames'])
            else:
                print("please type request again or check to see if your input is a valid search")

        # returns a list in order of highest to lowest income tax states
        if (search == 'income tax') or (search == 'income taxes'):
            for state in data['states']:
                print(state['stateNames'], state['incomeTax'], "%")

        # terminates the run
        if search == 'quit':
            break


    f.close()




if __name__ == '__main__':
    main()


