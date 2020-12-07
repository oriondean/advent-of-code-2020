import re
import functools

regex_bag_parse = re.compile('(\w+\s\w+) bags contain (.*)')
regex_bag_contains_parse = re.compile('(\d+) (\w+\s\w+) bags?')


def parse_bag(raw_bag: str) -> dict:
    result = regex_bag_contains_parse.match(raw_bag)
    return {'count': int(result.group(1)), 'bag': result.group(2)}


def score(scored_bag) -> int:
    if len(scored_bag['bags']) == 0:
        return 0
    else:
        bags = map(
            lambda bag: {'times_contained': bag['count'], 'bags': bags_dict[bag['bag']]['bags']}, scored_bag['bags']
        )
        return functools.reduce(
            lambda memo, bag: memo + (bag['times_contained'] + (bag['times_contained'] * score(bag))), bags, 0
        )


def find_bags_holding_color(bags, colours: list[str]) -> list[str]:
    return [b['name'] for b in bags if any(item['bag'] in colours for item in b['bags'])]


if __name__ == '__main__':
    bags_list = []
    bags_dict = {}

    with open('input.txt') as file:
        for line in file:
            match = regex_bag_parse.match(line.strip())
            raw_bags = match.group(2).split(', ')

            if raw_bags[0] == 'no other bags.':
                bag = {'name': match.group(1), 'bags': []}
                bags_dict[match.group(1)] = bag
                bags_list.append({'name': match.group(1), 'bags': []})
            else:
                bag = {'name': match.group(1), 'bags': list(map(parse_bag, raw_bags))}
                bags_dict[match.group(1)] = bag
                bags_list.append(bag)

    file.close()

    target = 'shiny gold'
    bags_directly_containing_target = find_bags_holding_color(bags_list, [target])
    bags_containing_target = set(bags_directly_containing_target)
    bags_found = bags_directly_containing_target
    while len(bags_found) > 0:
        bags_found = find_bags_holding_color(bags_list, bags_found)
        bags_containing_target |= set(bags_found)

    print('Part one', len(bags_containing_target))
    print('Part two', score(bags_dict[target]))
