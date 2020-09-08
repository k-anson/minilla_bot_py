# Planned Features

## Opt-out channel system
  - Bot will allow opt-out reaction options to remove you from channels you never want to see
    - Avoid clutter from # of channels
    - Avoid @here @everyone notifications
    - Avoid appearing in channel member list

## Inactive channel system
  - All channels in a particular category will be monitored for recent messages
    - Once every day the bot will identify any inactive channels and move them to the inactive category
      - A notification will be sent at the same time to inform users of the change
  - All channels in the inactive channel will be monitored for recent messages
    - Any message within an inactive channel will automatically see the channel moved back into the active channels category

## Calendar and events
  - Calendar channel will be used to a host a single message by the bot resembling a calendar for upcoming events
    - Calender events will link to events channel post for corresponding event
  - Events channel will be used to display detailed event information and allow interaction via emotes
    - Event created messages in respective channels will allow similar interactions
  - Bot commands allow anyone to create an event by providing some base information for it
  - Event owner can cancel the event or pass ownership to another person at any time
  - Bot can be instructed to alert users to upcoming event at given intervals (week of, day of, etc)
### Calendar Commands
  - `!cal create <calendar channel id> <events channel id> <?default>`
    - create calendar in db
    - create calendar embed
    - update db with calendar embed message id
  - `!calevent create <event name> <event time> <event description>`
    - create event in db
    - send event message in events channel
    - respond with link to event message
    - update calendar embed