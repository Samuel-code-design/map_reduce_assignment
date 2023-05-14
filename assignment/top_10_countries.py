from mrjob.job import MRJob
from mrjob.step import MRStep

class AICount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_top_10_countries, reducer=self.reducer_top_10_countries),
        ]

    def mapper_top_10_countries(self, country, count):
        # Emit (key, value) pair: (None, (count, country))
        yield None, (count, country)

    def reducer_top_10_countries(self, _, country_counts):
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

#local computer:
#python top_10_countries.py --output-dir ./top_10_countries AI.csv

