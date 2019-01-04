while 1:
    q1 = input('Is the car silent when you turn the key? y/n')
    if q1 == 'y':
        while 1:
            q11 = input('Are the battery terminals corroded? y/n')
            if q11 == 'y':
                print('단자를 깨끗하게 하고 다시 시도하라.')
                break
            elif q11 == 'n':
                print('케이블을 교체하고 다시 시도하라')
                break
            else:
                print('Invalid')
        break
    elif q1 == 'n':
        while 1:
            q2 = input('차에서 달깍거리는 소리가 나는가? y/n')
            if q2 == 'y':
                print('배터리를 교체하고 다시 시도하라')
                break
            elif q2 == 'n':
                while 1:
                    q22 = input('시동이 완전히 걸리지 않는가? y/n')
                    if q22 == 'y':
                        print('점화플러그 연결 상태를 점검하라.')
                        break
                    elif q22 == 'n':
                        while 1:
                            q222 = input('엔진이 동작한 후 바로 꺼지는가? y/n')
                            if q222 == 'n':
                                print('답이 없다')
                                break
                            elif q222 == 'y':
                                while 1:
                                    q2221 = input('차에 연료 분사 장치가 있는가? y/n')
                                    if q2221 == 'y':
                                        print('초크가 제대로 여닫히는지 확인하라.')
                                        break
                                    elif q2221 == 'n':
                                        print('서비스센터에 의뢰하라.')
                                        break
                                    else:
                                        print('Invalid')
                                break
                            else:
                                print('Invalid')
                        break
                    else:
                        print('Invalid')
                break
            else:
                print('Invalid')
        break
    else:
        print('Invalid')