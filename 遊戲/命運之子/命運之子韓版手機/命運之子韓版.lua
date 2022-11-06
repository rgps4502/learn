-- startApp("com.linegames.dcglobal")
-- ========== Settings ================
Settings:setCompareDimension(true, 1080) --模擬器寬
Settings:setScriptDimension(true, 1080)
Settings:set('MinSimilarity', 0.83) --圖片精準度
-- Settings:autoGameArea(true) --導航條必須要有

-- =========區域=======
-- Region:highlight() -- 讓紅色框框出現 ex: night:highlight() 再調用一次消失
--PVP----------------------------
night = Region(531, 982, 200, 180) --點擊夜世界
pvp_night = Region(211, 918, 200, 180) --點擊夜世界pvp
pvp_refresh = Region(570, 445, 200, 180) --刷新對戰列表
pvp_auto_config = Region(570, 400, 200, 180) --自動對戰設定
pvp_start = Region(380, 1090, 180, 80) --確認
pvp_start1 = Region(470, 690, 180, 80) --pvp開始
pvp_no_ticket = Region(498, 1266, 120, 315) --pvp票券不夠
pvp_over = Region(160, 878, 410, 40) --pvp結束
pvp_over1 = Region(91, 874, 539, 40) --pvp獎勵
pvp_over_2 = Region(328, 716, 100, 80) --pvp獎勵滿通知
reward = Region(560, 509, 120, 80) --pvp獎勵領取
reward1 = Region(167, 562, 400, 65) --pvp獎勵通知
reward_confirm = Region(460, 866, 120, 80) --pvp獎勵領取
reward_OK = Region(320, 800, 120, 80) --pvp獎勵確認
money_box = Region(926, 494, 150, 150) --買體力 點主畫面的箱子
touch_money = Region(273, 1829, 100, 100)
money_buy = Region(632, 1727, 156, 100)
----------------------------------------↑pvp

--練肥---------------------------
checkpoint = Region(884, 1535, 150, 90) --點擊刷圖
fight_setting = Region(813, 499, 260, 120) --設定刷關
choose_setting = Region(192, 1290, 250, 150) --點選關卡模式
choose_setting1 = Region(637, 2034, 120, 110) --點選關卡模式
fight_setting_count = Region(517, 1153, 50, 65) --設定刷關
fight_start = Region(464, 1619, 160, 60) --設定刷關
fight_end = Region(490, 1866, 110, 70) --刷關完成
food_full = Region(282, 1854, 75, 75) --腳色滿
agate = Region(774, 1460, 100, 100) --點擊獎盃
agate_point = Region(909, 1560, 120, 60) --點選叫出瑪瑙按鈕
agate_2 = Region(413, 2113, 250, 75) --進入瑪瑙
choose = Region(879, 1063, 80, 80) --選擇換成瑪瑙的腳色
choose_confirm = Region(441, 2113, 200, 75) -- 點擊確認
choose_ok = Region(704, 1300, 100, 100) -- 點擊確認
agate_exit = Region(488, 2112, 110, 80) --離開瑪瑙
exit = Region(984, 119, 80, 80) --離開瑪瑙頁面
MXA30 = Region(166, 882, 30, 35) --肥料滿等通知
MXA_confirm = Region(318, 1000, 110, 48) --肥料滿等確認
leavl_20 = Region(203, 271, 40, 50) --肥料等級20
leavl_check3star = Region(184, 318, 70, 60) --確認星數
right_20 = Region(520, 303, 65, 65) --右側第一格肥料等級20
star3 = Region(132, 595, 76, 28) --肥料判斷3星
star2 = Region(781, 595, 55, 30) --肥料判斷2星
join_team = Region(175, 630, 193, 90) --加入隊伍
exit_team = Region(491, 1766, 100, 60) --離開隊伍介面

--打reider---------------------------------------
go_reder = Region(386, 1681, 325, 100)
fight_redier = Region(854, 667, 200, 210)
redier_die = Region(892, 1622, 178, 160)
send_killer_redier = Region(560, 801, 66, 66)
redier_kill = Region(16, 790, 132, 131)
redier_fight = Region(896, 1285, 135, 65)
redier_kill_mode = Region(851, 552, 200, 55)
redier_kill_level30 = Region(27, 582, 150, 900)
redier_wait_level30 = Region(88, 512, 112, 50)

--打好友
friend_pk = Region(69, 330, 160, 80)
pk = Region(769, 580, 110, 1110) --開始PK
victory = Region(371, 755, 300, 300) --戰鬥結束勝利
lose = Region(482, 997, 112, 70) --戰鬥結束失敗
--==========  main program ===========
function pvp() --打pvp
    night:existsClick('night.png', 5) --點擊夜世界
    if pvp_night:exists('pvp_night.png', 5) then
        while true do
            pvp_night:existsClick('pvp_night.png', 0) --點擊夜世界pvp
            sleep(1)
            if not pvp_night:exists('pvp_night.png', 0) then
                break
            end
        end
    end
    while (true) do
        sleep(1)
        pvp_refresh:existsClick('pvp_refresh.png', 0) --刷新對戰列表
        sleep(2)
        pvp_auto_config:existsClick('pvp_auto_config.png', 2) --自動對戰設定
        pvp_start:existsClick('pvp_start.png', 2) --確認
        pvp_start1:existsClick('pvp_start1.png', 2) --pvp開始
        repeat
            sleep(5)
        until pvp_over:exists('pvp_over.png', 0) or pvp_over1:exists('pvp_over1.png', 0) or
            pvp_no_ticket:exists('no_ticket.png', 0) or
            reward1:exists('reward1.png', 0) or
            reward:exists('reward.png', 0) or
            pvp_over1:exists('pvp_over3.png', 0)

        if pvp_no_ticket:exists('no_ticket.png', 0) and feed_food == true then
            pvp_no_ticket:existsClick('no_ticket.png', 0)
            --沒有票了回到主畫面
            exit:existsClick('exit.png', 3)
            sleep(1)
            exit:existsClick('exit.png', 3)
            break
        else
            pvp_no_ticket:existsClick('no_ticket.png', 0)
        end
        if pvp_over1:exists('pvp_over3.png', 0) then --獎勵池滿
            click(Location(359, 952))
            sleep(1)
            if reward1:exists('reward1.png', 0) then
                click(Location(356, 736))
                sleep(1)
                click(Location(611, 526))
                sleep(1)
                reward:existsClick('reward.png', 1) --領取PVP獎勵
                reward_confirm:existsClick('pvp_start1.png', 1) --領取PVP確認
                reward_OK:existsClick('agate_exit.png', 1)
            elseif pvp_over1:exists('pvp_over1.png', 0) then --領取PVP獎勵
                click(Location(365, 950))
                pvp_over_2:existsClick('agate_exit.png', 1)
                sleep(1)
                reward:existsClick('reward.png', 1) --領取PVP獎勵
                reward_confirm:existsClick('pvp_start1.png', 1) --領取PVP確認
                sleep(1)
                reward_OK:existsClick('agate_exit.png', 1)
            else
                click(Location(365, 950))
            end
        end
    end
    --等帶回主畫面
    repeat
        sleep(2)
    until checkpoint:exists('checkpoint.png', 0)
end

function friend_PVP() --打好友
    --設定要移動的位置距離
    p1 = Location(392, 971)
    p2 = Location(392, 203)
    -- maxDistance: 每次移動最遠距離，如果移動距離超過，會插入每次多個距離為maxDistance的移動點，初始值為5
    -- insertWaitTimeMs: 如果需要插入移動點，會再前面同時插入等待insertWaitTime毫秒(millisecond)，初始值為1
    -- 調整適當的參數，可以在速度與正確性取得平衡
    setManualTouchParameter(150, 1)
    actionList = {
        {action = 'touchDown', target = p1}, --設定actionlist P1點按下
        {action = 'wait', target = 0.4}, --等待0.4秒
        {action = 'touchMove', target = p2}, --移動到p2點
        {action = 'wait', target = 0.4}, --等待0.4秒
        {action = 'touchUp', target = p2}
    } --放開
    if not friend_pk:exists('friend.png', 0) then
        click(Location(996, 2236))
    end
    while (true) do
        if pk:exists('pk.png', 0) then
            pk:existsClick('pk.png', 0)
            sleep(5)
            repeat
                sleep(3)
            until victory:existsClick('victory.png', 0) or lose:existsClick('lose.png', 0) or
                friend_pk:exists('friend.png', 0) or
                pk:exists('pk.png', 0)
            sleep(5)
        else
            repeat
                manualTouch(actionList) --調用actionList 無障礙7.0不支援 -- swipe(Location(555, 1000), Location(555, 530))
            until pk:exists('pk.png', 0.7)
        end
    end
end

function food(hot, star) --練肥
    --如果沒有找到戰鬥按鈕就重主介面尋找球圖標
    if not fight_setting:exists('fight_setting.png', 1) then
        if checkpoint:existsClick('checkpoint.png', 30) then --點擊刷圖
            choose_setting:existsClick('choose_setting.png', 5)
            choose_setting1:existsClick('choose_setting1.png', 2)
            click(Location(676, 653))
            click(Location(550, 750))
            if star == '三星' then
                --設定要移動的位置距離
                p1 = Location(395, 1329)
                p2 = Location(395, 860)
                -- maxDistance: 每次移動最遠距離，如果移動距離超過，會插入每次多個距離為maxDistance的移動點，初始值為5
                -- insertWaitTimeMs: 如果需要插入移動點，會再前面同時插入等待insertWaitTime毫秒(millisecond)，初始值為1
                -- 調整適當的參數，可以在速度與正確性取得平衡
                setManualTouchParameter(150, 1)
                actionList = {
                    {action = 'touchDown', target = p1}, --設定actionlist P1點按下
                    {action = 'wait', target = 0.4}, --等待0.4秒
                    {action = 'touchMove', target = p2}, --移動到p2點
                    {action = 'wait', target = 0.4}, --等待0.4秒
                    {action = 'touchUp', target = p2}
                } --放開
                manualTouch(actionList)
                sleep(0.6)
                click(Location(834, 2096))
            elseif star == '二星' then
                sleep(0.5)
                click(Location(834, 2096))
            end
        end
    end
    while (true) do
        time = os.date('%H')
        if hot == '是' then
            if time == '17' then
                repeat
                    sleep(10)
                    time = os.date('%H')
                until time == '18'
            end
            if (time == '18') or (time == '19') then
                --檢查是否滿級先換肥料
                if leavl_20:exists('leavl20.png', 0) and not leavl_check3star:exists('leavl_check3star.png', 0) then
                    click(Location(534, 453)) --進入隊伍花面
                    sleep(1)
                    food20_max20()
                    sleep(2)
                elseif leavl_20:exists('leavl30.png', 0) then
                    click(Location(534, 453)) --進入隊伍花面
                    sleep(1)
                    food20_max20()
                    sleep(2)
                end

                --3星打六場
                if fight_setting:exists('fight_setting.png', 0) then --設定刷關
                    fight_setting:existsClick('fight_setting.png', 0)
                    sleep(1)
                    if fight_setting_count:exists('fight_setting_count.png', 0) then
                        if star == '三星' then
                            repeat
                                click(Location(755, 1192))
                            until fight_setting_count:exists('fight_setting_count6.png', 0)
                        elseif star == '二星' then
                            repeat
                                click(Location(755, 1192))
                            until fight_setting_count:exists('fight_setting_count2.png', 0)
                        end
                        fight_start:existsClick('fight_start.png', 0)
                        if food_full:exists('food_full.png', 1) then --如果腳色滿了 執行換瑪瑙
                            food_full:existsClick('food_full.png', 0)
                            foods_full()
                        else
                            sleep(0.5)
                            click(Location(742, 1314))
                        end
                        fight_end:existsClick('no_ticket.png', 60)
                    end
                end
                sleep(2)
                if MXA30:exists('food_MAX30.png', 1) or MXA30:exists('food_MAX20.png', 1) then --肥料滿等
                    click(Location(915, 698))
                    sleep(0.7)
                    click(Location(534, 453)) --進入隊伍花面
                    sleep(1)
                    food20_max20()
                    sleep(2)
                elseif go_reder:exists('go_reder.png', 5) then --判斷打redier介面
                    go_reder:existsClick('go_reder.png', 1)
                    if fight_redier:exists('fight_redier.png', 30) then
                        sleep(3)
                        fight_redier:existsClick('fight_redier.png', 0)
                    end
                    repeat
                        sleep(4)
                    until redier_die:exists('redier_die.png', 0) or redier_kill:exists('redier_kill.png', 0) or
                        pvp_no_ticket:exists('no_ticket.png', 0) --等待打完 點球回主畫面
                    if redier_die:exists('redier_die.png', 0) or redier_kill:exists('redier_kill.png', 0) then
                        sleep(2)
                        redier_kill:existsClick('redier_kill.png', 2)
                        redier_die:existsClick('redier_die.png', 2)
                        exit:wait('exit.png', 30)
                        sleep(2)
                        if not send_killer_redier:exists('send_killer_redier.png', 2) then
                            exit:existsClick('exit.png', 0) --如果沒有辦法發送殺手模式就離開
                            sleep(5)
                        else
                            send_killer_redier:exists('send_killer_redier.png', 0) --發送殺手模式
                            sleep(1)
                            send_killer_redier:existsClick('send_killer_redier.png', 0) --發送殺手模式
                            pvp_no_ticket:existsClick('no_ticket.png', 10)
                            sleep(3)
                            exit:existsClick('exit.png', 3)
                        end
                    elseif pvp_no_ticket:exists('no_ticket.png', 0) then --如果沒體力直接離開
                        pvp_no_ticket:existsClick('no_ticket.png', 0)
                        exit:existsClick('exit.png', 1)
                        sleep(3)
                        if send_killer_redier:exists('send_killer_redier.png', 30) then --發送殺手模式
                            sleep(1)
                            send_killer_redier:existsClick('send_killer_redier.png', 0) --發送殺手模式
                            sleep(3)
                            pvp_no_ticket:existsClick('no_ticket.png', 2)
                            exit:existsClick('exit.png', 1)
                        end
                    end
                    break
                end
            else
                print('不是加倍時段', time)
                exit()
            end
        end
    end
end

function food20_max20() --當肥料20等換肥
    if star3:exists('star3.png', 0) or star3:exists('star2.png', 0) then --更換拿下星子
        swipe(Location(222, 455), Location(222, 922)) --第1格
        wait(0.6)
        swipe(Location(374, 455), Location(374, 922)) --第二格
        wait(0.6)
        swipe(Location(537, 455), Location(537, 922)) --第三格
        wait(0.6)
        swipe(Location(708, 455), Location(696, 922)) --第四格
        wait(0.6)
        swipe(Location(864, 455), Location(830, 922)) --第5格
    end
    sleep(0.7)
    star2:waitVanish('star2.png', 60) --等待60秒肥料被更換拉下
    --換肥邏輯
    while not star2:exists('star2.png', 0) do
        if not star2:exists('star2.png', 0) then
            click(Location(446, 1044))
            join_team:existsClick('join_team.png', 0)
            if join_team:exists('join_team.png', 0) then
                sleep(1)
            elseif pvp_no_ticket:existsClick('no_ticket.png', 0) then
            end
        end
    end
    exit_team:existsClick('agate_exit.png', 0)
end

function foods_full() --換瑪瑙
    if not agate:exists('agate.png', 2) then
        agate_point:existsClick('agate_point.png', 0)
        agate:existsClick('agate.png', 2)
        agate_2:existsClick('agate_2.png', 1)
    else
        agate:existsClick('agate.png', 2)
        agate_2:existsClick('agate_2.png', 1)
    end

    choose:existsClick('choose.png', 5)
    choose_confirm:existsClick('choose_confirm.png', 1)
    choose_ok:existsClick('choose_ok.png', 1)
    agate_exit:existsClick('agate_exit.png', 60)
    agate_exit:waitVanish('agate_exit.png', 60)
    exit:existsClick('exit.png', 1)
    choose_confirm:waitVanish('choose_confirm.png', 30)
    exit:existsClick('exit.png', 1)
    agate_2:waitVanish('agate_2.png', 20)
    exit_team:existsClick('agate_exit.png', 0)
end

function buy_h() ---用錢買體力
    if money_box:exists('money_box.png', 1) then
        while true do
            money_box:existsClick('money_box.png', 0)
            sleep(1)
            if not money_box:exists('money_box.png', 0) then
                break
            end
        end
    end

    touch_money:existsClick('touch_money.png', 0)
    click(Location(742, 1280))
    if money_buy:exists('money_buy.png', 1) then
        while true do
            money_buy:existsClick('money_buy.png', 0)
            click(Location(742, 1280))
        end
    end
end

function redier_f() --打redier
    redier_fight:existsClick('redier_fight.png', 0)
    sleep(2)
    while (true) do
        if redier_kill_mode:exists('redier_kill_mode.png', 20) then
            sleep(2)
            if redier_kill_mode:exists('redier_kill_mode.png', 0) then
                repeat
                    redier_kill_mode:existsClick('redier_kill_mode.png', 0)
                until not redier_kill_mode:exists('redier_kill_mode.png', 0)
            end
            redier_kill_mode:waitVanish('redier_kill_mode.png', 10)
            if not redier_kill_level30:exists('redier_kill_level30.png', 20) then --沒有30等目標
                redier_wait_level30:existsClick('redier_wait_level30.png', 400) --等待五分鐘點擊刷新
            else
                if redier_kill_level30:exists('redier_kill_level30.png', 20) then
                    if redier_kill_level30:exists('redier_kill_level30.png', 0) then
                        sleep(0.5)
                        redier_kill_level30:existsClick('redier_kill_level30.png', 2)
                        if fight_redier:exists('fight_redier.png', 30) then
                            repeat
                                fight_redier:existsClick('fight_redier.png', 0)
                            until not fight_redier:exists('fight_redier.png', 0) or
                                pvp_no_ticket:exists('no_ticket.png', 0)
                        end
                        repeat
                            sleep(4)
                        until redier_die:exists('redier_die.png', 0) or redier_kill:exists('redier_kill.png', 0) or
                            pvp_no_ticket:exists('no_ticket.png', 0) --等待打完 點球回主畫面
                    end
                    if redier_die:exists('redier_die.png', 0) or redier_kill:exists('redier_kill.png', 0) then
                        sleep(2)
                        redier_kill:existsClick('redier_kill.png', 2)
                        redier_die:existsClick('redier_die.png', 2)
                        -- exit:wait('exit.png', 30)
                        sleep(2)
                        if not send_killer_redier:exists('send_killer_redier.png', 0) then
                            sleep(0.5) --如果沒有辦法發送殺手模式就等待0.5
                        else
                            send_killer_redier:exists('send_killer_redier.png', 0) --發送殺手模式
                            sleep(1)
                            send_killer_redier:existsClick('send_killer_redier.png', 0) --發送殺手模式
                            pvp_no_ticket:existsClick('no_ticket.png', 10)
                            sleep(3)
                        end
                    elseif pvp_no_ticket:exists('no_ticket.png', 0) then --如果沒體力直接離開
                        pvp_no_ticket:existsClick('no_ticket.png', 0)
                        sleep(3)
                        exit:existsClick('exit.png', 0)
                        sleep(0.7)
                        click(Location(1008, 505))
                        print('沒有票券了')
                        exit(1)
                    end
                end
            end
        end
    end
end

--==使用者自訂=========
-- 按鈕選單
allTroops1 = {
    '是',
    '否'
}
allTroops2 = {
    '三星',
    '二星'
}
dialogInit()
addCheckBox('feed_food', '練肥', false) --是否打練肥
addCheckBox('hotTime', '加倍時段', false) --是否打練肥
addSpinner('hot', allTroops1, allTroops1[1]) --選擇關卡的群組按鈕
addSpinner('star', allTroops2, allTroops1[1]) --選擇關卡的群組按鈕
newRow() --換下一排
addCheckBox('pvp_fight', 'pvp', false) --是否打PVP
addCheckBox('friend', '朋友決鬥', false) --是否打好友
newRow() --換下一排
addCheckBox('buy', '用錢買體力', false) --是用錢買體力
addCheckBox('redierkill', '打redier', false) --是用錢買體力
dialogShowFullScreen('關卡設定')

while (true) do
    --用錢買體力
    if buy == true then
        buy_h()
    end
    -- 打PVP
    if pvp_fight == true then
        pvp()
    end
    --練肥
    if feed_food == true then
        food(hot, star)
    end
    -- 打好友
    if friend == true then
        friend_PVP()
    end
    if redierkill == true then
        redier_f()
    end
end

-- redier_kill_level30:highlight()
-- if redier_kill_level30:exists('redier_kill_level30.png', 2) then
--     print('yes')
-- else
--     print('no')
-- end
