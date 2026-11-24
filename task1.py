MIN_AGGREGATE = 75
MIN_SUBJECT_SCORE = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input())

eligible = []

for _ in range(n):
    data = input().split()

    applicant_id = data[0]
    aggregate = float(data[1])
    attendance = float(data[2])
    income = float(data[3])
    subject_count = int(data[4])
    subject_scores = list(map(float, data[5:5 + subject_count]))

    qualifies = (
        aggregate >= MIN_AGGREGATE
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
        and len(subject_scores) == subject_count
        and all(score >= MIN_SUBJECT_SCORE for score in subject_scores)
    )

    if qualifies:
        eligible.append((applicant_id, aggregate, attendance, income))

eligible.sort(key=lambda applicant: (
    -applicant[1],
    -applicant[2],
    applicant[3],
    applicant[0]
))

if not eligible:
    print("No eligible applicants")
else:
    print("Rank ID Aggregate Attendance Income")
    for rank, applicant in enumerate(eligible, start=1):
        applicant_id, aggregate, attendance, income = applicant
        print(f"{rank} {applicant_id} {aggregate:.2f} {attendance:.2f} {income:.2f}")



output

3
50
75
80
300000
3
Asha
90
85
80
95
250000
Ravi
80
80
80
90
200000
Mina
88
88
88
95
280000
