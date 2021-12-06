# Token API
curl -i -X POST -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     https://bankssearch-app.herokuapp.com/bank-data/auth/token/ \
     -d "{\"username\": \"admin\",\"password\": \"qwerty@1234\"}"

# Token Refresh API
curl -i -X POST -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     https://bankssearch-app.herokuapp.com/bank-data/auth/token/refresh/ \
     -d "{\"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODg1MzQ3NCwiaWF0IjoxNjM4NzY3MDc0LCJqdGkiOiIyZDc5NjNiZDFmNDE0YzI5OGMxNDdmOTk5NGExMWEyNSIsInVzZXJfaWQiOjF9.9XhpWc21ShJWAFSoDiemr49yEEKR33FBy-JsBkCbJ1U\"}"
     
# API to find out Bank Data by ifsc
curl -i GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4NzY4MTkwLCJpYXQiOjE2Mzg3NjcwNzQsImp0aSI6IjBmN2YwYWVkZjIwYjQ0NGRiYjgxMzJiOGQxZmY5MWZmIiwidXNlcl9pZCI6MX0.IieNb0-edR5_bCo_EaVFUUdaOjhFltaYwj4q0cN1ie8" \
     https://bankssearch-app.herokuapp.com/bank-data/branch/FDRL0002074/

# API to find out Branch Datas by bank name and city with offset and limit
curl -i GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4NzY5MjgwLCJpYXQiOjE2Mzg3NjcwNzQsImp0aSI6ImQ4MjA5MTg5ZmU3NTQ1MGQ5MGYwOWMyYzhkN2MyOTU1IiwidXNlcl9pZCI6MX0.-JDzlujTbezUhzKBWBGm3Sv4FpQXd-aE6NWxghp7e7E" \
     https://bankssearch-app.herokuapp.com/bank-data/branches/?city=THIMMAPURAM&bank_name=ANDHRA PRAGATHI GRAMEENA BANK&offset=1&limit=1

# API to find out Branch Datas by bank name and city with out offset and limit
curl -i GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4NzY5MjgwLCJpYXQiOjE2Mzg3NjcwNzQsImp0aSI6ImQ4MjA5MTg5ZmU3NTQ1MGQ5MGYwOWMyYzhkN2MyOTU1IiwidXNlcl9pZCI6MX0.-JDzlujTbezUhzKBWBGm3Sv4FpQXd-aE6NWxghp7e7E" \
     https://bankssearch-app.herokuapp.com/bank-data/branches/?city=THIMMAPURAM&bank_name=ANDHRA PRAGATHI GRAMEENA BANK