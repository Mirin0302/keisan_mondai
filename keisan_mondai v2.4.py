# coding: utf-8

print('アプリ名:keisan_mondai.py バージョン:v2.4_seisakubu')
print('このアプリは、全部で25問の計算問題があります')
print('途中から凄く難しくなりますが、頑張ってください!')
print('裏モードもあります! 問題は変わりませんが、おまけ機能なので、裏モードを探してみてください!')
print('このアプリは、Python 3.xで動作を確認しています')
print('このアプリのライセンスは、MITライセンスです')
print('MITライセンス日本語訳 https://ja.osdn.net/projects/opensource/wiki/licenses%2FMIT_license')
print('keisan_mondai.py GitHub ')
print('')

start = raw_input('始めるにはEnterを押してください: ')
if start == 'ura':
    
    point = input('[裏モード]正解するごとにもらえるポイントの点数を設定してください: ')

    name = raw_input('あなたの名前を教えてください: ')
    quiz_number = 1
    quiz = input('第' + str(quiz_number) + '問 1+1の答えは何ですか?: ')

    if quiz == 2:
    
        print('')
        print('------------------------------------')
        print('正解です!')
        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
        print('------------------------------------')
        print('')

        quiz_number = 2
        quiz = input('第' + str(quiz_number) + '問 7+8の答えは何ですか?: ')
    
        if quiz == 15:
            
            print('')
            print('------------------------------------')
            print('正解です!')
            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
            print('------------------------------------')
            print('')
    
            quiz_number = 3
            quiz = input('第' + str(quiz_number) + '問 17+19の答えは何ですか?: ')
    
            if quiz == 36:
                
                print('')
                print('------------------------------------')
                print('正解です!')
                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                print('------------------------------------')
                print('')

                quiz_number = 4
                quiz = input('第' + str(quiz_number) + '問 29+32の答えは何ですか?: ')

                if quiz == 61:
                    
                    print('')
                    print('------------------------------------')
                    print('正解です!')
                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                    print('------------------------------------')
                    print('')

                    quiz_number = 5
                    quiz = input('第' + str(quiz_number) + '問 48+79の答えは何ですか?: ')

                    if quiz == 127:
                    
                        print('')
                        print('------------------------------------')
                        print('正解です!')
                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                        print('------------------------------------')
                        print('')

                        quiz_number = 6
                        quiz = input('第' + str(quiz_number) + '問 86+63の答えは何ですか?: ')

                        if quiz == 149:
                        
                            print('')
                            print('------------------------------------')
                            print('正解です!')
                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                            print('------------------------------------')
                            print('')
    
                            quiz_number = 7
                            quiz = input('第' + str(quiz_number) + '問 108+157の答えは何ですか?: ')

                            if quiz == 265:
                            
                                print('')
                                print('------------------------------------')
                                print('正解です!')
                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                print('------------------------------------')
                                print('')
    
                                quiz_number = 8
                                quiz = input('第' + str(quiz_number) + '問 264+548の答えは何ですか?: ')

                                if quiz == 812:
                                
                                    print('')
                                    print('------------------------------------')
                                    print('正解です!')
                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                    print('------------------------------------')
                                    print('')
    
                                    quiz_number = 9
                                    quiz = input('第' + str(quiz_number) + '問 1086+249の答えは何ですか?: ')

                                    if quiz == 1335:
                                
                                        print('')
                                        print('------------------------------------')
                                        print('正解です!')
                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                        print('------------------------------------')
                                        print('')
        
                                        quiz_number = 10
                                        quiz = input('第' + str(quiz_number) + '問 2015+1894の答えは何ですか?: ')

                                        if quiz == 3909:
                                    
                                            print('')
                                            print('------------------------------------')
                                            print('正解です!')
                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                            print('------------------------------------')
                                            print('')
        
                                            quiz_number = 11
                                            quiz = input('第' + str(quiz_number) + '問 4098+4876の答えは何ですか?: ')

                                            if quiz == 8974:
                                        
                                                print('')
                                                print('------------------------------------')
                                                print('正解です!')
                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                print('------------------------------------')
                                                print('')
            
                                                quiz_number = 12
                                                quiz = input('第' + str(quiz_number) + '問 1×6の答えは何ですか?: ')

                                                if quiz == 6:
                                            
                                                    print('')
                                                    print('------------------------------------')
                                                    print('正解です!')
                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                    print('------------------------------------')
                                                    print('')
            
                                                    quiz_number = 13
                                                    quiz = input('第' + str(quiz_number) + '問 10×9の答えは何ですか?: ')

                                                    if quiz == 90:
                                                
                                                        print('')
                                                        print('------------------------------------')
                                                        print('正解です!')
                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                        print('------------------------------------')
                                                        print('')
            
                                                        quiz_number = 14
                                                        quiz = input('第' + str(quiz_number) + '問 10×0×7の答えは何ですか?: ')

                                                        if quiz == 0:
                                                    
                                                            print('')
                                                            print('------------------------------------')
                                                            print('正解です!')
                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                            print('------------------------------------')
                                                            print('')
            
                                                            quiz_number = 15
                                                            quiz = input('第' + str(quiz_number) + '問 9×8×6の答えは何ですか?: ')

                                                            if quiz == 432:
                                                            
                                                                print('')
                                                                print('------------------------------------')
                                                                print('正解です!')
                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                print('------------------------------------')
                                                                print('')
            
                                                                quiz_number = 16
                                                                quiz = input('第' + str(quiz_number) + '問 16×9×14の答えは何ですか?: ')

                                                                if quiz == 2016:
                                                            
                                                                    print('')
                                                                    print('------------------------------------')
                                                                    print('正解です!')
                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                    print('------------------------------------')
                                                                    print('')
            
                                                                    quiz_number = 17
                                                                    quiz = input('第' + str(quiz_number) + '問 24×18×65の答えは何ですか?: ')

                                                                    if quiz == 28080:
                                                            
                                                                        print('')
                                                                        print('------------------------------------')
                                                                        print('正解です!')
                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                        print('------------------------------------')
                                                                        print('')
            
                                                                        quiz_number = 18
                                                                        quiz = input('第' + str(quiz_number) + '問 2048÷4の答えは何ですか? ')

                                                                        if quiz == 512:
                                                                
                                                                            print('')
                                                                            print('------------------------------------')
                                                                            print('正解です!')
                                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                            print('------------------------------------')
                                                                            print('')
            
                                                                            quiz_number = 19
                                                                            quiz = input('第' + str(quiz_number) + '問 16÷0.04の答えは何ですか? ')

                                                                            if quiz == 400:
                                                                    
                                                                                print('')
                                                                                print('------------------------------------')
                                                                                print('正解です!')
                                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                print('------------------------------------')
                                                                                print('')
            
                                                                                quiz_number = 20
                                                                                quiz = input('第' + str(quiz_number) + '問 0.04÷200の答えは何ですか? ')

                                                                                if quiz == 0.0002:
                                                                        
                                                                                    print('')
                                                                                    print('------------------------------------')
                                                                                    print('正解です!')
                                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                    print('------------------------------------')
                                                                                    print('')
            
                                                                                    quiz_number = 21
                                                                                    quiz = input('第' + str(quiz_number) + '問 1597÷8の答えは何ですか? 小数第3位まで答えてください ')

                                                                                    if quiz == 199.625:
                                                                            
                                                                                        print('')
                                                                                        print('------------------------------------')
                                                                                        print('正解です!')
                                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                        print('------------------------------------')
                                                                                        print('')
            
                                                                                        quiz_number = 22
                                                                                        quiz = input('第' + str(quiz_number) + '問 1873-672の答えは何ですか? ')

                                                                                        if quiz == 1201:
                                                                                
                                                                                            print('')
                                                                                            print('------------------------------------')
                                                                                            print('正解です!')
                                                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                            print('------------------------------------')
                                                                                            print('')
            
                                                                                            quiz_number = 23
                                                                                            quiz = input('第' + str(quiz_number) + '問 487-589の答えは何ですか? ')

                                                                                            if quiz == -102:
                                                                                    
                                                                                                print('')
                                                                                                print('------------------------------------')
                                                                                                print('正解です!')
                                                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                print('------------------------------------')
                                                                                                print('')
            
                                                                                                quiz_number = 24
                                                                                                quiz = input('第' + str(quiz_number) + '問 5674-2653の答えは何ですか? ')

                                                                                                if quiz == 3021:
                                                                                        
                                                                                                    print('')
                                                                                                    print('------------------------------------')
                                                                                                    print('正解です!')
                                                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                    print('------------------------------------')
                                                                                                    print('')
            
                                                                                                    quiz_number = 24
                                                                                                    quiz = input('第' + str(quiz_number) + '問 426×8-5072の答えは何ですか? ')

                                                                                                    if quiz == -1664:
                                                                                            
                                                                                                        print('')
                                                                                                        print('------------------------------------')
                                                                                                        print('正解です!')
                                                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                        print('------------------------------------')
                                                                                                        print('')
            
                                                                                                        quiz_number = 25
                                                                                                        quiz = input('第' + str(quiz_number) + '問 789×256-104689+458×9の答えは何ですか? ')

                                                                                                        if quiz == 879777:
                                                                                                
                                                                                                            print('')
                                                                                                            print('------------------------------------')
                                                                                                            print('正解です!')
                                                                                                            print('ゲーム終了!!!')
                                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                            print('------------------------------------')
                                                                                                            print('')
            
                                                                                                            

                                                                                                        else:
                    
                                                                                                            print('')
                                                                                                            print('------------------------------------')
                                                                                                            print('違います!')
                                                                                                            quiz_number_result = quiz_number - 1
                                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                            print('終了します')
                                                                                                            print('------------------------------------')
                                                                                                            print('')

                                                                                                    else:
                
                                                                                                        print('')
                                                                                                        print('------------------------------------')
                                                                                                        print('違います!')
                                                                                                        quiz_number_result = quiz_number - 1
                                                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                        print('終了します')
                                                                                                        print('------------------------------------')
                                                                                                        print('')

                                                                                                else:
                
                                                                                                    print('')
                                                                                                    print('------------------------------------')
                                                                                                    print('違います!')
                                                                                                    quiz_number_result = quiz_number - 1
                                                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                    print('終了します')
                                                                                                    print('------------------------------------')
                                                                                                    print('')

                                                                                            else:
                
                                                                                                print('')
                                                                                                print('------------------------------------')
                                                                                                print('違います!')
                                                                                                quiz_number_result = quiz_number - 1
                                                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                print('終了します')
                                                                                                print('------------------------------------')
                                                                                                print('')

                                                                                        else:
                
                                                                                            print('')
                                                                                            print('------------------------------------')
                                                                                            print('違います!')
                                                                                            quiz_number_result = quiz_number - 1
                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                            print('終了します')
                                                                                            print('------------------------------------')
                                                                                            print('')

                                                                                    else:
                
                                                                                        print('')
                                                                                        print('------------------------------------')
                                                                                        print('違います!')
                                                                                        quiz_number_result = quiz_number - 1
                                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                        print('終了します')
                                                                                        print('------------------------------------')
                                                                                        print('')

                                                                                else:
                
                                                                                    print('')
                                                                                    print('------------------------------------')
                                                                                    print('違います!')
                                                                                    quiz_number_result = quiz_number - 1
                                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                    print('終了します')
                                                                                    print('------------------------------------')
                                                                                    print('')

                                                                            else:
            
                                                                                print('')
                                                                                print('------------------------------------')
                                                                                print('違います!')
                                                                                quiz_number_result = quiz_number - 1
                                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                print('終了します')
                                                                                print('------------------------------------')
                                                                                print('')

                                                                        else:
            
                                                                            print('')
                                                                            print('------------------------------------')
                                                                            print('違います!')
                                                                            quiz_number_result = quiz_number - 1
                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                            print('終了します')
                                                                            print('------------------------------------')
                                                                            print('')

                                                                    else:
            
                                                                        print('')
                                                                        print('------------------------------------')
                                                                        print('違います!')
                                                                        quiz_number_result = quiz_number - 1
                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                        print('終了します')
                                                                        print('------------------------------------')
                                                                        print('')

                                                                else:
            
                                                                    print('')
                                                                    print('------------------------------------')
                                                                    print('違います!')
                                                                    quiz_number_result = quiz_number - 1
                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                    print('終了します')
                                                                    print('------------------------------------')
                                                                    print('')

                                                            else:
            
                                                                print('')
                                                                print('------------------------------------')
                                                                print('違います!')
                                                                quiz_number_result = quiz_number - 1
                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                print('終了します')
                                                                print('------------------------------------')
                                                                print('')

                                                        else:
            
                                                            print('')
                                                            print('------------------------------------')
                                                            print('違います!')
                                                            quiz_number_result = quiz_number - 1
                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                            print('終了します')
                                                            print('------------------------------------')
                                                            print('')

                                                    else:
            
                                                        print('')
                                                        print('------------------------------------')
                                                        print('違います!')
                                                        quiz_number_result = quiz_number - 1
                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                        print('終了します')
                                                        print('------------------------------------')
                                                        print('')

                                                else:
            
                                                    print('')
                                                    print('------------------------------------')
                                                    print('違います!')
                                                    quiz_number_result = quiz_number - 1
                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                    print('終了します')
                                                    print('------------------------------------')
                                                    print('')

                                            else:
            
                                                print('')
                                                print('------------------------------------')
                                                print('違います!')
                                                quiz_number_result = quiz_number - 1
                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                print('終了します')
                                                print('------------------------------------')
                                                print('')

                                        else:
            
                                            print('')
                                            print('------------------------------------')
                                            print('違います!')
                                            quiz_number_result = quiz_number - 1
                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                            print('終了します')
                                            print('------------------------------------')
                                            print('')

                                    else:
            
                                        print('')
                                        print('------------------------------------')
                                        print('違います!')
                                        quiz_number_result = quiz_number - 1
                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                        print('終了します')
                                        print('------------------------------------')
                                        print('')
    

                                else:
            
                                    print('')
                                    print('------------------------------------')
                                    print('違います!')
                                    quiz_number_result = quiz_number - 1
                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                    print('終了します')
                                    print('------------------------------------')
                                    print('')
    

                            else:
            
                                print('')
                                print('------------------------------------')
                                print('違います!')
                                quiz_number_result = quiz_number - 1
                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                print('終了します')
                                print('------------------------------------')
                                print('')


                        else:
        
                            print('')
                            print('------------------------------------')
                            print('違います!')
                            quiz_number_result = quiz_number - 1
                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                            print('終了します')
                            print('------------------------------------')
                            print('')


                    else:
        
                        print('')
                        print('------------------------------------')
                        print('違います!')
                        quiz_number_result = quiz_number - 1
                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                        print('終了します')
                        print('------------------------------------')
                        print('')


                else:
        
                    print('')
                    print('------------------------------------')
                    print('違います!')
                    quiz_number_result = quiz_number - 1
                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                    print('終了します')
                    print('------------------------------------')
                    print('')


            else:
        
                print('')
                print('------------------------------------')
                print('違います!')
                quiz_number_result = quiz_number - 1
                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                print('終了します')
                print('------------------------------------')
                print('')


        else:
        
            print('')
            print('------------------------------------')
            print('違います!')
            quiz_number_result = quiz_number - 1
            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
            print('終了します')
            print('------------------------------------')
            print('')


    else:

        print('')
        print('------------------------------------')
        print('違います!')
        quiz_number_result = quiz_number - 1
        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
        print('終了します')
        print('------------------------------------')
        print('')

else:
    
    point = 1
    name = raw_input('あなたの名前を教えてください: ')
    quiz_number = 1
    quiz = input('第' + str(quiz_number) + '問 1+1の答えは何ですか?: ')

    if quiz == 2:
        
        print('')
        print('------------------------------------')
        print('正解です!')
        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
        print('------------------------------------')
        print('')

        quiz_number = 2
        quiz = input('第' + str(quiz_number) + '問 7+8の答えは何ですか?: ')
    
        if quiz == 15:
            
            print('')
            print('------------------------------------')
            print('正解です!')
            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
            print('------------------------------------')
            print('')
    
            quiz_number = 3
            quiz = input('第' + str(quiz_number) + '問 17+19の答えは何ですか?: ')
    
            if quiz == 36:
                
                print('')
                print('------------------------------------')
                print('正解です!')
                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                print('------------------------------------')
                print('')

                quiz_number = 4
                quiz = input('第' + str(quiz_number) + '問 29+32の答えは何ですか?: ')

                if quiz == 61:
                    
                    print('')
                    print('------------------------------------')
                    print('正解です!')
                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                    print('------------------------------------')
                    print('')

                    quiz_number = 5
                    quiz = input('第' + str(quiz_number) + '問 48+79の答えは何ですか?: ')

                    if quiz == 127:
                    
                        print('')
                        print('------------------------------------')
                        print('正解です!')
                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                        print('------------------------------------')
                        print('')

                        quiz_number = 6
                        quiz = input('第' + str(quiz_number) + '問 86+63の答えは何ですか?: ')

                        if quiz == 149:
                        
                            print('')
                            print('------------------------------------')
                            print('正解です!')
                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                            print('------------------------------------')
                            print('')
    
                            quiz_number = 7
                            quiz = input('第' + str(quiz_number) + '問 108+157の答えは何ですか?: ')

                            if quiz == 265:
                            
                                print('')
                                print('------------------------------------')
                                print('正解です!')
                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                print('------------------------------------')
                                print('')
    
                                quiz_number = 8
                                quiz = input('第' + str(quiz_number) + '問 264+548の答えは何ですか?: ')

                                if quiz == 812:
                                
                                    print('')
                                    print('------------------------------------')
                                    print('正解です!')
                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                    print('------------------------------------')
                                    print('')
    
                                    quiz_number = 9
                                    quiz = input('第' + str(quiz_number) + '問 1086+249の答えは何ですか?: ')

                                    if quiz == 1335:
                                
                                        print('')
                                        print('------------------------------------')
                                        print('正解です!')
                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                        print('------------------------------------')
                                        print('')
        
                                        quiz_number = 10
                                        quiz = input('第' + str(quiz_number) + '問 2015+1894の答えは何ですか?: ')

                                        if quiz == 3909:
                                    
                                            print('')
                                            print('------------------------------------')
                                            print('正解です!')
                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                            print('------------------------------------')
                                            print('')
        
                                            quiz_number = 11
                                            quiz = input('第' + str(quiz_number) + '問 4098+4876の答えは何ですか?: ')

                                            if quiz == 8974:
                                        
                                                print('')
                                                print('------------------------------------')
                                                print('正解です!')
                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                print('------------------------------------')
                                                print('')
            
                                                quiz_number = 12
                                                quiz = input('第' + str(quiz_number) + '問 1×6の答えは何ですか?: ')

                                                if quiz == 6:
                                            
                                                    print('')
                                                    print('------------------------------------')
                                                    print('正解です!')
                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                    print('------------------------------------')
                                                    print('')
            
                                                    quiz_number = 13
                                                    quiz = input('第' + str(quiz_number) + '問 10×9の答えは何ですか?: ')

                                                    if quiz == 90:
                                                
                                                        print('')
                                                        print('------------------------------------')
                                                        print('正解です!')
                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                        print('------------------------------------')
                                                        print('')
            
                                                        quiz_number = 14
                                                        quiz = input('第' + str(quiz_number) + '問 10×0×7の答えは何ですか?: ')

                                                        if quiz == 0:
                                                    
                                                            print('')
                                                            print('------------------------------------')
                                                            print('正解です!')
                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                            print('------------------------------------')
                                                            print('')
            
                                                            quiz_number = 15
                                                            quiz = input('第' + str(quiz_number) + '問 9×8×6の答えは何ですか?: ')

                                                            if quiz == 432:
                                                            
                                                                print('')
                                                                print('------------------------------------')
                                                                print('正解です!')
                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                print('------------------------------------')
                                                                print('')
            
                                                                quiz_number = 16
                                                                quiz = input('第' + str(quiz_number) + '問 16×9×14の答えは何ですか?: ')

                                                                if quiz == 2016:
                                                            
                                                                    print('')
                                                                    print('------------------------------------')
                                                                    print('正解です!')
                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                    print('------------------------------------')
                                                                    print('')
            
                                                                    quiz_number = 17
                                                                    quiz = input('第' + str(quiz_number) + '問 24×18×65の答えは何ですか?: ')

                                                                    if quiz == 28080:
                                                            
                                                                        print('')
                                                                        print('------------------------------------')
                                                                        print('正解です!')
                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                        print('------------------------------------')
                                                                        print('')
            
                                                                        quiz_number = 18
                                                                        quiz = input('第' + str(quiz_number) + '問 2048÷4の答えは何ですか? ')

                                                                        if quiz == 512:
                                                                
                                                                            print('')
                                                                            print('------------------------------------')
                                                                            print('正解です!')
                                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                            print('------------------------------------')
                                                                            print('')
            
                                                                            quiz_number = 19
                                                                            quiz = input('第' + str(quiz_number) + '問 16÷0.04の答えは何ですか? ')

                                                                            if quiz == 400:
                                                                    
                                                                                print('')
                                                                                print('------------------------------------')
                                                                                print('正解です!')
                                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                print('------------------------------------')
                                                                                print('')
            
                                                                                quiz_number = 20
                                                                                quiz = input('第' + str(quiz_number) + '問 0.04÷200の答えは何ですか? ')

                                                                                if quiz == 0.0002:
                                                                        
                                                                                    print('')
                                                                                    print('------------------------------------')
                                                                                    print('正解です!')
                                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                    print('------------------------------------')
                                                                                    print('')
            
                                                                                    quiz_number = 21
                                                                                    quiz = input('第' + str(quiz_number) + '問 1597÷8の答えは何ですか? 小数第3位まで答えてください ')

                                                                                    if quiz == 199.625:
                                                                            
                                                                                        print('')
                                                                                        print('------------------------------------')
                                                                                        print('正解です!')
                                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                        print('------------------------------------')
                                                                                        print('')
            
                                                                                        quiz_number = 22
                                                                                        quiz = input('第' + str(quiz_number) + '問 1873-672の答えは何ですか? ')

                                                                                        if quiz == 1201:
                                                                                
                                                                                            print('')
                                                                                            print('------------------------------------')
                                                                                            print('正解です!')
                                                                                            print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                            print('------------------------------------')
                                                                                            print('')
            
                                                                                            quiz_number = 23
                                                                                            quiz = input('第' + str(quiz_number) + '問 487-589の答えは何ですか? ')

                                                                                            if quiz == -102:
                                                                                    
                                                                                                print('')
                                                                                                print('------------------------------------')
                                                                                                print('正解です!')
                                                                                                print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                print('------------------------------------')
                                                                                                print('')
            
                                                                                                quiz_number = 24
                                                                                                quiz = input('第' + str(quiz_number) + '問 5674-2653の答えは何ですか? ')

                                                                                                if quiz == 3021:
                                                                                        
                                                                                                    print('')
                                                                                                    print('------------------------------------')
                                                                                                    print('正解です!')
                                                                                                    print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                    print('------------------------------------')
                                                                                                    print('')
            
                                                                                                    quiz_number = 24
                                                                                                    quiz = input('第' + str(quiz_number) + '問 426×8-5072の答えは何ですか? ')

                                                                                                    if quiz == -1664:
                                                                                            
                                                                                                        print('')
                                                                                                        print('------------------------------------')
                                                                                                        print('正解です!')
                                                                                                        print(str(name) + 'さんの現在のポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                        print('------------------------------------')
                                                                                                        print('')
            
                                                                                                        quiz_number = 25
                                                                                                        quiz = input('第' + str(quiz_number) + '問 789×256-104689+458×9の答えは何ですか? ')

                                                                                                        if quiz == 879777:
                                                                                                
                                                                                                            print('')
                                                                                                            print('------------------------------------')
                                                                                                            print('正解です!')
                                                                                                            print('ゲーム終了!!!')
                                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number * point)) + '点です!')
                                                                                                            print('------------------------------------')
                                                                                                            print('')
            
                                                                                                            

                                                                                                        else:
                    
                                                                                                            print('')
                                                                                                            print('------------------------------------')
                                                                                                            print('違います!')
                                                                                                            quiz_number_result = quiz_number - 1
                                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                            print('終了します')
                                                                                                            print('------------------------------------')
                                                                                                            print('')

                                                                                                    else:
                
                                                                                                        print('')
                                                                                                        print('------------------------------------')
                                                                                                        print('違います!')
                                                                                                        quiz_number_result = quiz_number - 1
                                                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                        print('終了します')
                                                                                                        print('------------------------------------')
                                                                                                        print('')

                                                                                                else:
                
                                                                                                    print('')
                                                                                                    print('------------------------------------')
                                                                                                    print('違います!')
                                                                                                    quiz_number_result = quiz_number - 1
                                                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                    print('終了します')
                                                                                                    print('------------------------------------')
                                                                                                    print('')

                                                                                            else:
                
                                                                                                print('')
                                                                                                print('------------------------------------')
                                                                                                print('違います!')
                                                                                                quiz_number_result = quiz_number - 1
                                                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                                print('終了します')
                                                                                                print('------------------------------------')
                                                                                                print('')

                                                                                        else:
                
                                                                                            print('')
                                                                                            print('------------------------------------')
                                                                                            print('違います!')
                                                                                            quiz_number_result = quiz_number - 1
                                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                            print('終了します')
                                                                                            print('------------------------------------')
                                                                                            print('')

                                                                                    else:
                
                                                                                        print('')
                                                                                        print('------------------------------------')
                                                                                        print('違います!')
                                                                                        quiz_number_result = quiz_number - 1
                                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                        print('終了します')
                                                                                        print('------------------------------------')
                                                                                        print('')

                                                                                else:
                
                                                                                    print('')
                                                                                    print('------------------------------------')
                                                                                    print('違います!')
                                                                                    quiz_number_result = quiz_number - 1
                                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                    print('終了します')
                                                                                    print('------------------------------------')
                                                                                    print('')

                                                                            else:
            
                                                                                print('')
                                                                                print('------------------------------------')
                                                                                print('違います!')
                                                                                quiz_number_result = quiz_number - 1
                                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                                print('終了します')
                                                                                print('------------------------------------')
                                                                                print('')

                                                                        else:
            
                                                                            print('')
                                                                            print('------------------------------------')
                                                                            print('違います!')
                                                                            quiz_number_result = quiz_number - 1
                                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                            print('終了します')
                                                                            print('------------------------------------')
                                                                            print('')

                                                                    else:
            
                                                                        print('')
                                                                        print('------------------------------------')
                                                                        print('違います!')
                                                                        quiz_number_result = quiz_number - 1
                                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                        print('終了します')
                                                                        print('------------------------------------')
                                                                        print('')

                                                                else:
            
                                                                    print('')
                                                                    print('------------------------------------')
                                                                    print('違います!')
                                                                    quiz_number_result = quiz_number - 1
                                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                    print('終了します')
                                                                    print('------------------------------------')
                                                                    print('')

                                                            else:
            
                                                                print('')
                                                                print('------------------------------------')
                                                                print('違います!')
                                                                quiz_number_result = quiz_number - 1
                                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                                print('終了します')
                                                                print('------------------------------------')
                                                                print('')

                                                        else:
            
                                                            print('')
                                                            print('------------------------------------')
                                                            print('違います!')
                                                            quiz_number_result = quiz_number - 1
                                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                            print('終了します')
                                                            print('------------------------------------')
                                                            print('')

                                                    else:
            
                                                        print('')
                                                        print('------------------------------------')
                                                        print('違います!')
                                                        quiz_number_result = quiz_number - 1
                                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                        print('終了します')
                                                        print('------------------------------------')
                                                        print('')

                                                else:
            
                                                    print('')
                                                    print('------------------------------------')
                                                    print('違います!')
                                                    quiz_number_result = quiz_number - 1
                                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                    print('終了します')
                                                    print('------------------------------------')
                                                    print('')

                                            else:
            
                                                print('')
                                                print('------------------------------------')
                                                print('違います!')
                                                quiz_number_result = quiz_number - 1
                                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                                print('終了します')
                                                print('------------------------------------')
                                                print('')

                                        else:
            
                                            print('')
                                            print('------------------------------------')
                                            print('違います!')
                                            quiz_number_result = quiz_number - 1
                                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                            print('終了します')
                                            print('------------------------------------')
                                            print('')

                                    else:
            
                                        print('')
                                        print('------------------------------------')
                                        print('違います!')
                                        quiz_number_result = quiz_number - 1
                                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                        print('終了します')
                                        print('------------------------------------')
                                        print('')
    

                                else:
            
                                    print('')
                                    print('------------------------------------')
                                    print('違います!')
                                    quiz_number_result = quiz_number - 1
                                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                    print('終了します')
                                    print('------------------------------------')
                                    print('')
    

                            else:
            
                                print('')
                                print('------------------------------------')
                                print('違います!')
                                quiz_number_result = quiz_number - 1
                                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                                print('終了します')
                                print('------------------------------------')
                                print('')


                        else:
        
                            print('')
                            print('------------------------------------')
                            print('違います!')
                            quiz_number_result = quiz_number - 1
                            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                            print('終了します')
                            print('------------------------------------')
                            print('')


                    else:
        
                        print('')
                        print('------------------------------------')
                        print('違います!')
                        quiz_number_result = quiz_number - 1
                        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                        print('終了します')
                        print('------------------------------------')
                        print('')


                else:
        
                    print('')
                    print('------------------------------------')
                    print('違います!')
                    quiz_number_result = quiz_number - 1
                    print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                    print('終了します')
                    print('------------------------------------')
                    print('')


            else:
        
                print('')
                print('------------------------------------')
                print('違います!')
                quiz_number_result = quiz_number - 1
                print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
                print('終了します')
                print('------------------------------------')
                print('')


        else:
        
            print('')
            print('------------------------------------')
            print('違います!')
            quiz_number_result = quiz_number - 1
            print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
            print('終了します')
            print('------------------------------------')
            print('')


    else:

        print('')
        print('------------------------------------')
        print('違います!')
        quiz_number_result = quiz_number - 1
        print(str(name) + 'さんの最終的なポイントは、' + str(int(quiz_number_result * point)) + '点です')
        print('終了します')
        print('------------------------------------')
        print('')
