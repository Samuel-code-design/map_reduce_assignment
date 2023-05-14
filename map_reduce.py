from mrjob.job import MRJob
from mrjob.step import MRStep


class AICount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_combine, reducer=self.reducer_combine),
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper_combine(self, _, line):
        # Skip the header row (assuming it's the first row)
        if line[0].startswith('Country'):
            return

        # Extract the country column
        country = line[0]

        # Emit (key, value) pair: (country, 1) for count_countries
        yield "count_countries", (country, 1)

        # Emit (key, value) pair: ('Netherlands', 1) for count_netherlands
        if country == 'Netherlands':
            yield "count_netherlands", ('Netherlands', 1)

    def reducer_combine(self, key, values):
        if key == "count_countries":
            counts = {}

            # Sum the counts for each country
            for country, count in values:
                counts[country] = counts.get(country, 0) + count

            # Emit (key, value) pair: (country, count) for count_countries
            for country, count in counts.items():
                yield "count_countries", (country, count)

        elif key == "count_netherlands":
            # Sum the counts for the Netherlands
            count = sum(count for _, count in values)

            # Emit (key, value) pair: ('Number of companies from the Netherlands', count) for count_netherlands
            yield "count_netherlands", ('Number of companies from the Netherlands', count)

    def mapper(self, _, line):
        # Skip the header row (assuming it's the first row)
        if line.startswith('Country'):
            return

        # Split the line by comma
        fields = line.split(',')

        # Extract the country column
        country = fields[0]

        # Emit (key, value) pair: (None, (count, country))
        yield None, (1, country)

    def reducer(self, _, country_counts):
        # Initialize a list to store country counts
        top_countries = []

        # Iterate over the country counts and keep track of the top 10
        for count, country in country_counts:
            top_countries.append((count, country))
            top_countries = sorted(top_countries, reverse=True)[:10]

        # Emit the top 10 countries
        for count, country in top_countries:
            yield country, count


if __name__ == '__main__':
    AICount.run()
