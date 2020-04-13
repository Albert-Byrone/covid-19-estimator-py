def get_days(period, time_elapsed):
  if period == 'days':
      return time_elapsed

  if period == 'weeks':
      return time_elapsed * 7

  if period == 'months':
      return time_elapsed * 30

def estimator(data):
  return data
