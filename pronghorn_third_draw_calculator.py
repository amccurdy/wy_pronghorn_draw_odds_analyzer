#!/usr/bin/env python3

'''
take the text off of WY's website: https://wgfd.wyo.gov/Hunting/Drawing-Odds/2022-Drawing-Odds
and remove all the headers so it's just lines that look like this:
037 1 ANY ANTELOPE 5 0 14 3
then run this script alongside that text file
'''
 
f = open('antelope_odds_special_random.txt', 'r')
fl = f.readlines()
fl_clean = [x.strip() for x in fl]

hunts = []

for item in fl_clean: 
    itemsplit = item.split(' ')
    huntunit = {'unit_number': int(itemsplit[0]),
                'type': int(itemsplit[1]),
                'quota': int(itemsplit[4]),
                'first': int(itemsplit[5]),
                'second': int(itemsplit[6]),
                'third': int(itemsplit[7])}
    hunts.append(huntunit)


def find_thirds():
    possible_thirds = []
    for unit in hunts:
        # ignoring type 2 because those are private
        if unit['type'] == 2:
            pass
        total_applicants = unit['first'] + unit['second'] + unit['third']
        if unit['quota'] >= total_applicants:
            gmu_details = {'unit_number': unit['unit_number'], 'tot': total_applicants, 'quota': unit['quota']}
            possible_thirds.append(gmu_details)
    if len(possible_thirds) > 0:
        return possible_thirds
    else:
        return None

results = find_thirds()

if __name__ == '__main__':
    if results:
        for tp in results: 
            print('Unit {id} had {total} applicant(s) against a quota of {quota}'.format(id=tp['unit_number'], total=tp['tot'], quota=tp['quota']))
