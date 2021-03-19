# Code by Christopher Sommerville
# Span coding challenge

import json
import datetime
    
# Part 1 Methods

# Accepts a dictionary containing the old format of a notification JSON object
# Returns a new dictionary containing all of the old information but converted into the new format
def old_to_new(old: list):
    new_format_dict = {}

    # Convert timestamp
    new_format_dict['timestamp'] = get_epoch(old['datestring'])

    # Convert priority
    new_format_dict['priority'] = convert_priority(old['priority'])

    # Convert message by splitting old message into title and body
    old_message = old['msg'].split(':')
    new_format_dict['body'] = old_message[1][1:] # Skip beginning whitespace
    new_format_dict['title'] = old_message[0]

    # deduplication_id stays the same from old to new format
    new_format_dict['deduplication_id'] = old['deduplication_id']

    return new_format_dict

# Accepts a date in ISO 8601-format and returns the unix epoch timestamp in milliseconds
def get_epoch(date: str):
    # Z indicates zero UTC offset
    # Always true for sample data
    if date[len(date) - 1] == "Z":
        date = date[:len(date) - 1] + "+00:00"
    return int(datetime.datetime.fromisoformat(date).timestamp() * 1000)

# Accepts a string representing the priority level of a notification
# Converts the string into an integer representation
# Returns 2 for 'HIGH', 1 for 'MID', 0 for 'LOW', -1 for any other input
def convert_priority(priority_str: str):
    if priority_str == "HIGH":
        return 2
    elif priority_str == "MID":
        return 1
    elif priority_str == "LOW":
        return 0
    return -1

# Part 2 Methods

# Function that accepts a list of new format notifications
# Returns a list with duplicate notifications removed
# When notifications share an id, the higher priority notification is kept
# When notifications share an id and priority, the later timestamp is kept
def remove_duplicates(data: list):
    # Dictionary to hold pairs of deduplication ids and their notification data
    ids = {}

    # Iterate through each notification and update the ids dictionary
    for notification in data:
        dedup_id = notification['deduplication_id']
        
        if dedup_id in ids: # duplicate found
            curr_priority = notification['priority']
            old_priority = ids[dedup_id]['priority']
            if curr_priority == old_priority: # if equal priority, check timestamps
                curr_timestamp = notification['timestamp']
                old_timestamp = ids[dedup_id]['timestamp']
                if curr_timestamp > old_timestamp: # replace the older timestamped notification
                    ids[dedup_id] = notification
            elif curr_priority > old_priority: # replace lower priority notification
                ids[dedup_id] = notification
        else:
            ids[dedup_id] = notification

    # Copy deduplicated data into new list of notifications
    deduped_data = []
    for id in ids:
        deduped_data.append(ids[id])

    return deduped_data

# Part 3 Methods

# Accepts a list of notifications in the new format
# Returns a list of the notifications sorted in ascending order of timestamp then descending order by priority
# I.e. Older notifications appear in front of recent notifications
# For notifications with the same timestamp, higher priority notifications appear in front of lower priority notifications
def sort_notifications(data: list):
    
    # Sort by priority in descending order
    data.sort(key = lambda notification: notification['priority'], reverse=True)
    
    # Sort by timestamp in ascending order
    data.sort(key = lambda notification: notification['timestamp'])

