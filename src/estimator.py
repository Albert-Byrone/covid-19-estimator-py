def get_days(period, time_elapsed):
  if period == 'days':
      return time_elapsed

  if period == 'weeks':
      return time_elapsed * 7

  if period == 'months':
      return time_elapsed * 30

def get_currently_infected_people(data, output):
  reported_cases = data['reportedCases']
  output['impact']['currentlyInfected'] = reported_cases * 10
  output['severeImpact']['currentlyInfected'] = reported_cases * 50


def estimator(data):
  return data
