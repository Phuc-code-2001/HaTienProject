import pusher

pusher_client = pusher.Pusher(
  app_id='1610805',
  key='4dc578f3128e5c599631',
  secret='a1aef62bebf6e774c452',
  cluster='ap1',
  ssl=True
)


def send_notification(channels, data):
    pusher_client.trigger(channels, '-notification', data)
    