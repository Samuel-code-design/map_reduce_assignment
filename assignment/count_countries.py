from mrjob.job import MRJob
from mrjob.step import MRStep

class AICount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
        ]

    def mapper(self, _, line):
        # Skip the header row (assuming it's the first row)
        if line.startswith('Country'):
            return

        # Split the line by comma
        fields = line.split(',')

        # Extract the country column
        country = fields[0]

        # Emit (key, value) pair: (country, 1)
        yield country, 1

    def reducer(self, key, values):
        # Sum the counts for each country
        count = sum(values)

        # Emit (key, value) pair: (country, count)
        yield key, count

if __name__ == '__main__':
    AICount.run()

# local computer:
# python count_countries.py --output-dir ./count_countries AI.csv