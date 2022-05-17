from Query.querybuilder import foo


def main():
    with open('queries.txt') as file:
        queries = [line.rstrip() for line in file]
    for i, query in enumerate(queries, start=1): foo(query, i)


if __name__ == '__main__':
    main()