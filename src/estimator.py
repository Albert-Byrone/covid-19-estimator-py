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


def get_infections_by_requested_time(data, output):
  days = get_days(data['periodType'], data['timeToElapse'])
  output['impact']['infectionsByRequestedTime'] = int(output['impact']['currentlyInfected'] * (2 ** int(days / 3)))

  output['severeImpact']['infectionsByRequestedTime'] = int(output['severeImpact']['currentlyInfected'] * (2 ** int(days / 3)))

def estimator(data):
  return data
