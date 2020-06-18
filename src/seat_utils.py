class Seat(object):
    @staticmethod
    def read_input():
        output_seat_struct = []
        seat_partition = int(input('Enter total partition'))
        for each in range(0, seat_partition):
            row, column = map(int, input('Enter number of rows,columns seperated by comma').split(','))
            output_seat_struct.append([row,column])
        return output_seat_struct

    @staticmethod
    def is_valid(seat_struct,num_of_passengers):
        seating_capacity = 0
        for each in seat_struct:
            seating_capacity+=each[0]*each[1]
        if seating_capacity<num_of_passengers:
            return False
        return True
    @staticmethod
    def is_aisle_seat(each_side, column, seat_arrangement, i):
        """
        :param each_side: each side of the entire seat structure
        :param column: current column of each side
        :param seat_arrangement: total seat structure
        :param i: index of current seat side
        :return: True if the given seat if Aisle seat
        """
        if (each_side[1] < 2 and i == 0 and column != 0) or (each_side[1] == 2 and column != 0) or (
                0 < i < len(seat_arrangement) - 1 and (column == 0 or column == each_side[1] - 1)):
            return True

        elif column > 0 and column == each_side[1] - 1 and i == 0:
            return True

        elif i == len(seat_arrangement) - 1 and column == 0 and each_side[1] > 1:
            return True

    @staticmethod
    def is_window_seat(each_side, column, seat_arrangement, i):
        """
        Description : Checks if the given seat is window seat or not
        :param each_side: each side of the entire seat structure
        :param column: current column of each side
        :param seat_arrangement: total seat structure
        :param i: index of current seat side
        :return: True if the given seat if Window seat
        """
        if i == 0 and column == 0 or (i == 0 and column == 1 and each_side[1] == 2 and len(seat_arrangement) == 1):
            return True
        elif (i == len(seat_arrangement) - 1 and column == each_side[1] - 1) or (each_side[1] == 1):
            return True

    @staticmethod
    def assign_seat_number(max_rows, plane_seat, seat_structure, seat_type, seat_number, passengers_count):
        """
        :param max_rows: Maximum row in seat arrangement
        :param plane_seat: labelled seat arrangement
        :param seat_structure: numbered seat
        :param seat_type: A or W or < seat
        :param seat_number: current seat number
        :param passengers_count: Total count of passengers
        :return: seat number after updating
        """
        assigned_seat_list = []
        for row in range(0, max_rows):
            for i, each_side in enumerate(plane_seat):
                if row < len(each_side):
                    for column in range(len(each_side[1])):
                        if each_side[row][column] == seat_type:
                            if seat_number <= passengers_count:
                                seat_structure[i][row][column] = seat_number
                                assigned_seat_list.append(seat_number)
                                seat_number += 1
                            else:
                                seat_structure[i][row][column] = 'vacant'
        return seat_number,assigned_seat_list
    @staticmethod
    def get_max_row_column(seat_structure):
        """
        Description - gets the maximum number of rows and columns
        :param seat_structure: input seat structure
        :return: max_row,max_column
        """
        row_list = [x[0] for x in seat_structure]
        column_list = [x[1] for x in seat_structure]
        return max(row_list), max(column_list)
