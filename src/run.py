from observer import Observer

from subject import Subject


if __name__ == "__main__":
    subject = Subject()
    observer_1 = Observer("Наблюдатель 1")
    observer_2 = Observer("Наблюдатель 2")

    subject.attach(observer_1)
    subject.attach(observer_2)

    subject.set_data("данные для наблюдателя")