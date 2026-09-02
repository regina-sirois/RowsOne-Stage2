# RowsOne-Stage2: Strategy for Employee API tests

## Prioritization

Coming into a new situation, I am of course conferring with the engineering manager on priorities. However, as a quality professional, I also have opinions in this space. I like to start with tricky, critical logic, or areas of an application that have surfaced the most defects. The things developers are worrying about when their code is pushed to prod.

I prefer not to duplicate unit test coverage as much as possible, and I have been known to thin out integration tests that were adding no value. The focus is on ROI, given capacity is a limited thing. It is likely that you already know that the CRUD functionality works, but those are quick and easy and familiarize one with the API anyway, so it's not a bad place to begin. It surfaces questions like: where is an employee's gender and ethnicity set, as I do not see those in the employee POST or PUT requests?

Authentication tests are also high value due to security being a primary concern, but I haven't often found defects there - especially in comparison with **Data Integrity**, which seems to be a thorny issue for any company managing an extensive dataset over time. Performance testing is also valuable in some contexts - for endpoints managing a high valume of calls or on applications updating and maintaining a significant amount of state. 

For the **structure and order** of a test suite - it really depends on the application. However, my goal is always to keep everything clean and well-organized, easy to read and find, maintain a clear separation of test and framework code, and have documented [code/design standards](README.md#code-approach) enforced by linters & proper code reviews.

Some observations I made while I was working with this API are documented [here](results/README.md). 

---

## Validation

> **This is the meat of the testing exercise - a high priority target.**

- CRUD behavior of the API works as expected.
- Any logic triggered via the API or eventing is determined to behave as expected.
- Eventing (if applicable) works as expected - events are sent and received, idempotency, retries, DLQing, etc.
- Any timed behaviors (eg, a termination date passes, this causes a status to change...etc) are validated.
- Application behaviors are consistent and predictable, and performance is acceptable (via performance testing).

---

## API responses  

> **The following approach has been most expediant and efficient for me:**

**API responses** will be serialized into the checked-in generated models by the sevice client wrapper, passively validating the contract. In the event of a serialization failure, a ValueError will be raised with an explicit description of the expected and received types, and the calling test will fail.

Assertion comparisons of expected and received field values will validate that the data populated in the object is appropriate. These comparisons should be exhaustive without being overly brittle (for example, it would be brittle to assert on full string error descriptions preseving capitalization. Less so, finding a case-normalized keyword in an error).

API filtering fields and pagination settings (and boundaries) should also be validated to ensure no unexpected returns. API should comply with REST standards.

---



## Data integrity

> **Data integrity is often under-tested, but it's critical to application usability!**

- Required fields are actually required - and successfully backfilled if made required.
- Appropriate values are accepted (for example, the state abbreviations of MP (Northern Mariana Islands) and FM (Federated States of Micronesia) were rejected as invalid by the API. Are they?), and innappropriate values are rejected (such as perhaps john@gmail as an employee email, or a date_of_hire after an employees date_of_termination).
- Idempotent endpoints such as update_employee_details are actually idempotent.
- The data makes sense, for example: an employee has a specific position at a specific company, I would expect to find that company in a get_companies API call, and for that position to perhaps have an "active" status. If a company claims 75 employees, I would expect 75 employees to be returned by get_employees, filtered on that company. Two phones numbers can not both be primary, etc.
- Children of deleted parent objects are effectively handled (deleted or soft-deleted)
- Metadata associated with a response object is properly implemented (updated_at updates on writes, fields make sense)
- Any potential state transitions are valid and make sense.

---



## Authorization

> **Authorization validations include tests such as:**

- User permission validations: admin vs standard users, RBAC, etc, if applicable.
- api/login claims to implement account lockout and status checks - we should validate that it does both of those things properly.
- Requested scopes for any potential oauth tokens perform as expected, read can read but not write, write can read and write but potentially not delete, etc. Expired tokens no longer grant access. Invalid credentials cannot obtain tokens. (assuming eventual oauth).

---



## Boundary conditions

> **Boundary condition validations include tests such as:**

- how many employees can a company have? And how few? Probably not -1...how about 30 million?
- what date ranges are valid? Could an employee have a start date in 1931? Can they have a termination date two years from now?
- how large do profile pictures get to be? How many total notes is possible? Can an employee have 100 companies? etc.

---



## Error handling

> **Error handling validations include tests/concerns such as:**

- do malformed API requests generate 400 errors as expected? Does attempting to get an employee that doesn't exist generate a 404?
- do auth failures return the expected error codes (401, 403) in the correct situations?
- are there any unhandled exceptions (500's) in the course of testing/usage? Those should be investigated and handled.
- How are failures logged out, and what about observability, alerts, etc?
- if there are any retries on failures, what are potential side-effects?

---



## Test isolation and reliability

---

I enumerate some of my testing philsophy [here](README.md#test-philosophy), near the bottom of the document. Essentially, I believe that analysis, separating concerns, and testing isolated components/services is paramount to effective quality assurance. True end-to-end tests should be few, and cover common user behavioral patterns - most of the tests should be closer in. Nightly regression is a bit of an anti-pattern. Tests should gate releases and test ONLY those releases, as much as possible. 

Gating tests are a forcing function for reliable tests. But reliable tests are also written that way; they are pragmatic rather than hopeful.. for example, polling for a result vs. attempting to time one. There are valid use-cases for test retries - sh*t happens. Test data should be properly scoped and disambiguated so that collisions are extremely improbable. Tests should be short, and implement more or less probable scenarios, rather than outlandish or impossible ones. 


## Ice cream vs gelato

See [here](README.md#frozen-dessert-philosophy)