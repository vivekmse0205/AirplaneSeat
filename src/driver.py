from src import seat_utils
import sys
sys.path.insert(0,'../')
import copy
import json
if __name__ == '__main__':
    # Change this passenger count value to increase or decrease the passengers
    passengers_count = 30
    input_file_path = '../resources/input1.json'
    with open(input_file_path) as json_file:
        data = json.load(json_file)
    seat_arrangement = data['seat_struct']

    """
    Uncomment if you want to give hard-coded value or user input value
    """
    # To give a hard-coded value
    # seat_arrangement = [[2, 4], [4, 4], [3, 2], [4, 1]]

    # To read from user
    # seat_arrangement = seat_utils.Seat.read_input()
    if seat_utils.Seat.is_valid(seat_arrangement,passengers_count):
        aisle_seat_count = 0
        window_seat_count = 0
        middle_seat_count = 0
        max_rows,max_columns = seat_utils.Seat.get_max_row_column(seat_arrangement)

        plane_seat = []
        for i,each_side in enumerate(seat_arrangement):
            side_list = []
            for row in range(0,each_side[0]):
                row_list = []
                for column in range(0,each_side[1]):
                    if seat_utils.Seat.is_window_seat(each_side, column, seat_arrangement, i):
                        row_list.append('W')
                        window_seat_count+=1
                    elif seat_utils.Seat.is_aisle_seat(each_side, column, seat_arrangement, i):
                        row_list.append('A')
                        aisle_seat_count+=1
                    else:
                        row_list.append('M')
                        middle_seat_count+=1
                side_list.append(row_list)
            plane_seat.append(side_list)

        seat_structure = copy.deepcopy(plane_seat)
        seat_number = 1
        output_dict = {}
        for seat_type in ['A','W','M']:
            seat_number,seat_list = seat_utils.Seat.assign_seat_number(max_rows, plane_seat, seat_structure, seat_type, seat_number, passengers_count)
            output_dict[seat_type] = seat_list

        # Store the output as json file in current location
        with open('output.json','w') as json_file:
            json.dump(output_dict,json_file)

        print(f'Allotted seats are as \n')
        for each_side in seat_structure:
            print(each_side)
        print(f'Total aisle seat {aisle_seat_count} \nTotal Middle seat {middle_seat_count} \nTotal Window seat {window_seat_count}')
    else:
        print('Number of passengers is greater than available seats')




