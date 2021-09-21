# CHANGELOG

## v0.3.0 (2021-05-23)

* Properly escape double quotes in the message string
* Adds unit tests

## v0.2.0 (2021-05-15)

* Make `name` optional by fixing a `replace` bug when not present

## v0.1.0 (2021-05-14)

* Initial release
* Accepts a CSV with names and numbers
* `--force` flag to allow dry runs (great for larger lists)
* Send a single SMS message to individual numbers from a CSV (optional name can be passed to the iterated messages)
