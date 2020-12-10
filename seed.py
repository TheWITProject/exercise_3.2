# import your models

def seed(session):
    # write seed function here
    session = sessionmaker()

    software_design = Task(
        user_id = 1,
        name = "Lab 13",
        description = "Finish all parts of Lab 13",
        priority = 4,
        due_date = date(2020,13,12)
    )
    discrete_structures = Task(
        user_id = 2,
        name = "Homework #11",
        description = "Complete all 11 questions & upload",
        priority = 3,
        due_date = date(2020,14,12)

    )
    business_organization = Task(
        user_id = 3,
        name = "Problem Set #6",
        description = "Answer all questions and upload.",
        priority = 2,
        due_date = date(2020,15,12)
    )
    statistics = Task(
        user_id = 4,
        name = "Homework #5",
        description = "Complete all questions.",
        priority = 1,
        due_date = date(2020,16,12)
    )

    user_1 = User(
        name = "Naima"
    )
    user_2 = User(
        name = "Anna"
    )
    user_3 = User(
        name = "Shylee"
    )
    user_4 = User(
        name = "Olivia"
    )
    user_5 = User(
        name = "Anooj"
    )

    session.add([software_design, discrete_structures, business_organization, statistics, user_1,user_2,user_3,user_4,user_5])

    session.commit()
