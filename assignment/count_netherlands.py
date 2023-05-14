from mrjob.job import MRJob
from mrjob.step import MRStep

class AICount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_count_countries, reducer=self.reducer_count_countries),
            MRStep(mapper=self.mapper_count_netherlands, reducer=self.reducer_count_netherlands)
        ]

    def mapper_count_countries(self, _, line):
        # Skip the header row (assuming it's the first row)
        if line.startswith('Country'):
            return

        # Split the line by comma
        fields = line.split(',')

        # Extract the country column
        country = fields[0]

        # Emit (key, value) pair: (country, 1)
        yield country, 1

    def reducer_count_countries(self, key, values):
        # Sum the counts for each country
        count = sum(values)

        # Emit (key, value) pair: (country, count)
        yield key, count

    def mapper_count_netherlands(self, key, count):
        # Check if the country is the Netherlands
        if key == 'Netherlands':
            # Emit (key, value) pair: ('Netherlands', count)
            yield 'Netherlands', count

    def reducer_count_netherlands(self, key, values):
        # Sum the counts for the Netherlands
        count = sum(values)

        # Emit (key, value) pair: ('Number of companies from the Netherlands', count)
        yield 'Number of companies from the Netherlands', count

if __name__ == '__main__':
    AICount.run()

#local computer:
# python count_netherlands.py --output-dir ./count_netherlands AI.csv