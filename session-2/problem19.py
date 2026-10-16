'''
Session 2, Problem 19: Sensor log (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check which row of your structures table this is.

Write a class that records readings from sensors over time.

Class name: SensorLog

Creating a SensorLog() takes no arguments, and a new log starts empty.

For any one sensor, the timestamps in successive record calls always strictly increase.

Methods:

record(sensor, value, timestamp): sensor is a string, value is an int, timestamp is a non-negative int. Stores the reading. Returns the number of readings now stored for that sensor, as an int.
latest(sensor): sensor is a string. Returns the value of the sensor's most recent reading, as an int, or None if the sensor has no readings.
average(sensor): sensor is a string. Returns the average of all the sensor's reading values, as a float, or None if the sensor has no readings.

Session 2, Problem 19: Sensor log. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your SensorLog class. Everything from Level 1 must keep working.

New methods:

readings_between(sensor, start, end): sensor is a string; start and end are non-negative ints with start ≤ end. Returns a list of the sensor's reading values with timestamps from start to end, inclusive, in time order (earliest first). Returns an empty list if the sensor has no readings in that range or doesn't exist.
top_sensors(n): n is a non-negative int. Returns a list of the n sensors with the highest latest reading, each as a string in the format "sensor(value)", where value is that sensor's most recent reading. The list is sorted by value, largest first; sensors with equal values are sorted alphabetically by name. If there are fewer than n sensors, returns all of them.
'''

from typing import final


class SensorLog:
    
    def __init__(self):
        self.records: dict[str, dict] = {} # k= sensor (str), dict w/ k=ts, v= value
    
    '''1. record(sensor, value, timestamp): sensor is a string, value is an int, timestamp is a non-negative int. 
    Stores the reading. 
    Returns the number of readings now stored for that sensor, as an int.'''
    def record(self, sensor: str, value: int, timestamp: int):
        records_data = self.records.get(sensor, None)
        # If fist record, establish the inner dict
        if records_data is None:
            self.records[sensor] = {timestamp:value}
            readings = 1
        # If NOT fist record, add to the inner dict
        else:
            self.records[sensor][timestamp] = value
            # new len = old len + 1
            readings = len(records_data)
        # ret len of readings
        print(f'self.records[sensor]: {self.records[sensor]}, readings: {readings}')
        return readings
    
    '''2. latest(sensor): sensor is a string. 
    Returns the value of the sensor's most recent reading, as an int, or None if the sensor has no readings.'''
    def latest(self, sensor: str):
        records_data = self.records.get(sensor, None)
        print(f'records_data: {records_data}')
        # Return none if no readings
        if records_data is None:
            return None
        solution = list(records_data.values())[-1]
        print(f'solution: {solution}')
        return solution
    
    '''3. average(sensor): sensor is a string. 
    Returns the average of all the sensor's reading values, as a float, or None if the sensor has no readings.'''
    def average(self, sensor: str):
        records_data = self.records.get(sensor, None)
        print(f'records_data: {records_data}')
        # Return none if no readings
        if records_data is None:
            return None
        return sum(values for timestamps, values in records_data.items()) / len(records_data)

    '''readings_between(sensor, start, end): sensor is a string; start and end are non-negative ints with start ≤ end. 
    Returns a list of the sensor's reading values with timestamps from start to end, inclusive, in time order (earliest first). 
    Returns an empty list if the sensor has no readings in that range or doesn't exist.'''
    def readings_between(self, sensor: str, start: int, end: int):
        records_data = self.records.get(sensor, None)
        print(f'records_data: {records_data}')
        # Return none if no readings
        if records_data is None:
            return None
        # Get a list of reading between start and end
        return [reading for timestamp, reading in records_data.items() if (timestamp >= start and timestamp <= end)]
        solution = solution[start:end]
        print(f'solution: {solution}')
    
    '''top_sensors(n): n is a non-negative int. 
    Returns a list of the n sensors with the highest latest reading, each as a string in the format "sensor(value)", 
    where value is that sensor's most recent reading. The list is sorted by value, largest first; 
    sensors with equal values are sorted alphabetically by name. 
    If there are fewer than n sensors, returns all of them.'''
    def top_sensors(self, n: int):
        # Sort and convert to list
        sol_dict = {}
        for sensor, pairs in self.records.items():
            for timestamp, reading in pairs.items():
                sol_dict[sensor] = reading
        sol_list_sorted = [f'{sensor}({reading})' for sensor, reading in sorted(sol_dict.items(), key=lambda kv: (-kv[1], kv[0]))[:n]]
        print(f'sol_list: {sol_list_sorted}')
        return sol_list_sorted
        



# Complexity:
# r = total readings for a given sensor
# n = total readings across ALL sensors
# s = sensors
# 1. record -> O(1)        
# 2. latest --> copies dict to list --> O(r)
# 3. average --> loop --> O(r)

# worst case: O(r)
# memory: O(s + n)

# Example tests:

log = SensorLog()
assert log.record("temp", 20, 10) == 1
assert log.record("temp", 30, 20) == 2
assert log.latest("temp") == 30
assert log.latest("dog") is None # no reading

log = SensorLog()
log.record("temp", 20, 10)
log.record("temp", 30, 20)
assert log.average("temp") == 25.0


log = SensorLog()
log.record("temp", 20, 10)
log.record("temp", 25, 20)
log.record("temp", 30, 30)
assert log.readings_between("temp", 15, 30) == [25, 30]


log = SensorLog()
log.record("temp", 20, 10)
log.record("humidity", 60, 10)
log.record("temp", 70, 20)
assert log.top_sensors(2) == ["temp(70)", "humidity(60)"]