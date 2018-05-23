from Interval import Interval
from user_config import *

intervals = []

intervals.extend(Interval('unison', 0, 0, unison_prob) for _ in range(0, unison_prob))
intervals.extend(Interval('dim_second', 1, 0, diminished_second_prob) for _ in range(0, diminished_second_prob))

intervals.extend(Interval('aug_unison', 0, 1, augmented_unison_prob) for _ in range(0, augmented_unison_prob))
intervals.extend(Interval('min_second', 1, 1, minor_second_prob) for _ in range(0, minor_second_prob))

intervals.extend(Interval('maj_second', 1, 2, major_second_prob) for _ in range(0, major_second_prob))
intervals.extend(Interval('dim_third', 2, 2, diminished_third_prob) for _ in range(0, diminished_third_prob))

intervals.extend(Interval('aug_second', 1, 3, augmented_second_prob) for _ in range(0, augmented_second_prob))
intervals.extend(Interval('min_third', 2, 3, minor_third_prob) for _ in range(0, minor_third_prob))

intervals.extend(Interval('maj_third', 2, 4, major_third_prob) for _ in range(0, major_third_prob))
intervals.extend(Interval('dim_fourth', 3, 4, diminished_fourth_prob) for _ in range(0, diminished_fourth_prob))

intervals.extend(Interval('aug_third', 2, 5, augmented_third_prob) for _ in range(0, augmented_third_prob))
intervals.extend(Interval('fourth', 3, 5, fourth_prob) for _ in range(0, fourth_prob))

intervals.extend(Interval('aug_fourth', 3, 6, augmented_fourth_prob) for _ in range(0, augmented_fourth_prob))
intervals.extend(Interval('dim_fifth', 4, 6, diminished_fifth_prob) for _ in range(0, diminished_fifth_prob))

intervals.extend(Interval('fifth', 4, 7, fifth_prob) for _ in range(0, fifth_prob))
intervals.extend(Interval('dim_sixth', 5, 7, diminished_sixth_prob) for _ in range(0, diminished_sixth_prob))

intervals.extend(Interval('aug_fifth', 4, 8, augmented_fifth_prob) for _ in range(0, augmented_fifth_prob))
intervals.extend(Interval('min_sixth', 5, 8, minor_sixth_prob) for _ in range(0, minor_sixth_prob))

intervals.extend(Interval('maj_sixth', 5, 9, major_sixth_prob) for _ in range(0, major_sixth_prob))
intervals.extend(Interval('dim_seventh', 6, 9, diminished_seventh_prob) for _ in range(0, diminished_seventh_prob))

intervals.extend(Interval('aug_sixth', 5, 10, augmented_sixth_prob) for _ in range(0, augmented_sixth_prob))
intervals.extend(Interval('min_seventh', 6, 10, minor_seventh_prob) for _ in range(0, minor_seventh_prob))

intervals.extend(Interval('maj_seventh', 6, 11, major_seventh_prob) for _ in range(0, major_seventh_prob))
intervals.extend(Interval('dim_octave', 7, 11, diminished_octave_prob) for _ in range(0, diminished_octave_prob))

intervals.extend(Interval('aug_seventh', 6, 12, augmented_seventh_prob) for _ in range(0, augmented_seventh_prob))
intervals.extend(Interval('octave', 7, 12, octave_prob) for _ in range(0, octave_prob))

if __name__ == '__main__':
    for interval in intervals:
        print(interval.name)

    if not intervals:
        print("empty")
