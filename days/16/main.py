import re
from functools import reduce

def parse_rule(rule_raw):
    return {
        'field': rule_raw.group(1),
        'conditions': [
            list(map(int, rule_raw.group(2).split('-'))),
            list(map(int, rule_raw.group(3).split('-'))),
        ],
        'found': False,
        'col': -1,
    }


def read_input():
    tickets = []
    rules = []

    with open('input.txt') as file:
        for line in file:
            rule_match = regex_rule.match(line)
            if rule_match:
                rules.append(parse_rule(rule_match))
            elif regex_ticket.match(line):
                tickets.append(list(map(int, line.split(','))))

    return tickets, rules, tickets[0]

def passes_condition(condition, value):
    conditions = condition['conditions']
    return (conditions[0][0] <= value <= conditions[0][1]) or \
           (conditions[1][0] <= value <= conditions[1][1])


if __name__ == '__main__':
    regex_rule = re.compile('([\w\s]+): (\d+-\d+) or (\d+-\d+)')
    regex_ticket = re.compile('(\d+)+')

    [tickets, rules, ticket_own] = read_input()
    fields_invalid = []
    tickets_valid = tickets.copy()

    for ticket in tickets:
        for field in ticket:
            if not any([passes_condition(n, field) for n in rules]):
                fields_invalid.append(field)
                tickets_valid.remove(ticket)

    print('Part one', reduce(lambda memo, value: memo + value, fields_invalid))

    len_rules = len(rules)
    len_columns = len(ticket_own)
    tickets_columns = [[t[i] for t in tickets_valid] for i in range(0, len_columns)]
    rules_matched = []

    while len(rules_matched) < len_rules:
        for col in tickets_columns:
            rules_matching = [all([passes_condition(r, c) for c in col]) for r in rules]

            if reduce(lambda memo, value: memo + int(value), rules_matching) == 1:
                rule_matched = rules[rules_matching.index(True)]
                rule_matched['col'] = ticket_own.index(col[0])

                rules_matched.append(rule_matched)
                rules.remove(rule_matched)
                tickets_columns.remove(col)
                break

    rules_departures = [r for r in rules_matched if r['field'].startswith('departure')]

    print('Part two',
          reduce(lambda memo, value: memo * value, [ticket_own[r['col']] for r in rules_departures]))
