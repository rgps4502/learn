-- startApp("com.linegames.dcglobal")
-- ========== Settings ================
Settings:setCompareDimension(true, 1080) --模擬器寬
Settings:setScriptDimension(true, 1080)
Settings:set("MinSimilarity", 0.8)  	--圖片精準度

-- =========區域=======
-- Region:highlight() -- 讓紅色框框出現 ex: night:highlight() 再調用一次消失
--PVP----------------------------
-- night = Region(531, 982, 200, 180)  	--點擊夜世界
-- pvp_night = Region(147, 673, 200, 180)  	--點擊夜世界pvp
-- pvp_refresh = Region(570, 445, 200, 180)  	--刷新對戰列表
-- pvp_auto_config = Region(570, 400, 200, 180)  	--自動對戰設定
-- pvp_start = Region(380, 1090, 180, 80)  	--確認
-- pvp_start1 = Region(470, 690, 180, 80)  	--pvp開始
-- pvp_no_ticket = Region(325, 694, 110, 80)  	--pvp票券不夠
-- pvp_over = Region(160, 878, 410, 40)  	--pvp結束
-- pvp_over1 = Region(85, 874, 610, 40)  	--pvp獎勵
-- pvp_over_2 = Region(328, 716, 100, 80)  	--pvp獎勵滿通知
-- reward = Region(560, 509, 120, 80)  	--pvp獎勵領取
-- reward1 = Region(185, 500, 308, 50)  	--pvp獎勵通知
-- reward_confirm = Region(460, 866, 120, 80)  	--pvp獎勵領取
-- reward_OK =  Region(320, 800, 120, 80)  	--pvp獎勵確認
----------------------------------------↑pvp

--練肥---------------------------
checkpoint = Region(884, 1545, 200, 180) --點擊刷圖
pointnumber = Region(534, 573, 200, 80) --點擊4-6關卡
pointnumber2 = Region(0, 1280, 1080, 430) --點擊4-6-1關卡
fight_config = Region(866, 483, 200, 100) --設定輪迴條件
fight_confirm = Region(488, 1923, 200, 100) --輪迴條件確認
fight_start = Region(873, 754, 200, 100) --開始戰鬥
food_full = Region(136, 1644, 870, 50) --腳色滿
agate = Region(795, 1469, 300, 120) --點擊獎盃
agate_point = Region(913, 1568, 150, 80) --點選叫出瑪瑙按鈕
agate_2 = Region(420, 2116, 310, 80) --進入瑪瑙
choose = Region(873, 1059, 150, 150) --選擇換成瑪瑙的腳色
choose_confirm = Region(445, 2114, 250, 120) -- 點擊確認
choose_ok = Region(714, 1306, 110, 80) --離開瑪瑙
agate_exit = Region(488, 2110, 120, 80) -- 點擊確認
exit = Region(967, 118, 80, 80) --離開瑪瑙頁面
MXA = Region(147, 1643, 810, 49)  	--肥料滿等通知
MXA_confirm = Region(492, 1723, 110, 55)  	--肥料滿等確認
leavl_20 = Region(318, 1000, 110, 48)  	--肥料等級20
right_20 = Region(788, 539, 85, 85)  	--右側第一格肥料等級20
star3 = Region(297, 596, 120, 40)  	--肥料判斷3星
star2 = Region(783, 591, 120, 40)  	--肥料判斷2星
join_team = Region(191, 653, 240, 80) --加入隊伍
exit_team = Region(493, 1763, 160, 120) --離開隊伍介面


--打好友
-- friend_pk = Region(616, 1243, 110, 110) --進入好友頁面
-- pk = Region(511, 344, 80, 710) --開始PK
-- victory = Region(250, 573, 224, 52) --戰鬥結束勝利
-- lose = Region(322, 525, 73, 42) --戰鬥結束失敗
--==========  main program ===========
function pvp() --打pvp
  night:existsClick("night.png",5) --點擊夜世界
  pvp_night:existsClick("pvp_night.png",5) --點擊夜世界pvp
  while (true) do
    sleep(1)
    pvp_refresh:existsClick("pvp_refresh.png",0) --刷新對戰列表
    sleep(2)
    pvp_auto_config:existsClick("pvp_auto_config.png",2) --自動對戰設定
    pvp_start:existsClick("pvp_start.png",2) --確認
    pvp_start1:existsClick("pvp_start1.png",2) --pvp開始
    repeat
      sleep(5)
    until pvp_over:exists("pvp_over.png",0) or pvp_over1:exists("pvp_over1.png",0) or pvp_no_ticket:exists("no_ticket.png",0) or reward1:exists("reward1.png",0) or reward:exists("reward.png",0)
    if  pvp_no_ticket:exists("no_ticket.png",0) then
      pvp_no_ticket:existsClick("no_ticket.png",0)
      sleep(60)
    elseif reward1:exists("reward1.png",0) then
      click(Location(228, 760))
      sleep(1)
      click(Location(257, 1131))
      sleep(1)
      reward:existsClick("reward.png",1)  --領取PVP獎勵
      reward_confirm:existsClick("pvp_start1.png",1)  --領取PVP確認
      reward_OK:existsClick("agate_exit.png",1)
    elseif pvp_over1:exists("pvp_over1.png",0) then  --領取PVP獎勵
      click(Location(365, 950))
      pvp_over_2:existsClick("agate_exit.png",1)
      sleep(1)
      reward:existsClick("reward.png",1)  --領取PVP獎勵
      reward_confirm:existsClick("pvp_start1.png",1)  --領取PVP確認
      sleep(1)
      reward_OK:existsClick("agate_exit.png",1)
    else
      click(Location(365, 950))
    end
  end
end

function friend_PVP() --打好友
  --設定要移動的位置距離
  p1 = Location(392,971)
  p2 = Location(392,603)
  -- maxDistance: 每次移動最遠距離，如果移動距離超過，會插入每次多個距離為maxDistance的移動點，初始值為5
  -- insertWaitTimeMs: 如果需要插入移動點，會再前面同時插入等待insertWaitTime毫秒(millisecond)，初始值為1
  -- 調整適當的參數，可以在速度與正確性取得平衡
  setManualTouchParameter(5, 1)
  actionList = { {action = "touchDown", target = p1}, --設定actionlist P1點按下
      {action = "wait", target = 0.4}, --等待0.4秒
      {action = "touchMove", target = p2}, --移動到p2點
      {action = "wait", target = 0.4}, --等待0.4秒
      {action = "touchUp", target = p2} } --放開
  friend_pk:existsClick("friend.png",0)
  while (true)do
    if pk:exists("pk.png",0) then
      pk:existsClick("pk.png",0)
      sleep(5)
      repeat
        sleep (3)
      until victory:existsClick("victory.png",0) or lose:existsClick("lose.png",0) or friend_pk:exists("friend.png",0)
      sleep(5)
    else
      repeat
        manualTouch(actionList) --調用actionList
      until pk:exists("pk.png",0)
    end
  end
end
function food() --練肥
  if checkpoint:existsClick("checkpoint.png",0) then--點擊刷圖
    sleep(2)
    click(Location(540, 1827)) --選擇HARD
    sleep(1)
    click(Location(542, 1935)) --選擇第4關
    sleep(1)
    pointnumber:existsClick("4-6.png",2) --點擊4-6關卡
    sleep(2)
    pointnumber2:existsClick("4-6-1.png",2) --點擊4-6-1關卡
  end
  while (true) do
    if fight_config:exists("fight_config.png",5) then --設定戰鬥條件
      fight_config:existsClick("fight_config.png",2)
      sleep(1.5)
      click(Location(161, 862))
      if fight_confirm:exists("fight_confirm.png",0) then
        fight_confirm:existsClick("fight_confirm.png",0)
        fight_start:existsClick("fight_start.png",1) --開始戰鬥
      end
    end
    repeat
      sleep(3)
    until food_full:exists('food_full.png',0) or MXA:exists("food_MAX.png",0) or fight_config:exists("fight_config.png",0)
    if food_full:exists('food_full.png',0) then --如果腳色滿了 執行換瑪瑙
      click(Location(546,1755))
      sleep(1)
      click(Location(547,445)) --進入隊伍花面
      if not agate:exists("agate.png",2) then
        agate_point:existsClick("agate_point.png",0)
        agate:existsClick("agate.png",2)
        agate_2:existsClick("agate_2.png",1)
      else
        agate:existsClick("agate.png",2)
        agate_2:existsClick("agate_2.png",1)
      end
      choose:existsClick("choose.png",1)
      choose_confirm:existsClick("choose_confirm.png",1)
      choose_ok:existsClick("choose_ok.png",1)
      agate_exit:existsClick("agate_exit.png",10)
      exit:existsClick("exit.png",1)
      sleep(1)
      exit:existsClick("exit.png",1)
      sleep(1)
      if right_20:exists('leavl20.png',1) then  --如果同時肥料滿 又20等的設定(判斷最右邊的肥料是否20等) 判斷是否有肥料20等
        food20_max20()
        sleep(3)
      else
        exit:existsClick("exit.png",1)
        sleep(3)
      end
    elseif MXA:exists("food_MAX.png",0) then   --肥料滿等
      MXA_confirm:existsClick("MAX_confirm.png",0)
      sleep(1)
      click(Location(547,445)) --進入隊伍花面
      sleep(1)
      food20_max20()
      sleep(3)
    end
  end
end

function food20_max20()   --當肥料20等換肥
  if star3:exists("star3.png",0) then --如果第二格是2星就更換 1 更換 0 不更換
    c = 0
    swipe(Location(855,530),Location(855,886))    --最後一格
    wait(0.4)
    swipe(Location(710,530),Location(710,886))  --倒數第二格
    wait(0.4)
    swipe(Location(552,530),Location(547,886))  --倒數第三格
  else   --一帶四
    c = 1
    swipe(Location(855,530),Location(855,886))    --最後一格
    wait(0.4)
    swipe(Location(710,530),Location(710,886))  --倒數第二格
    wait(0.4)
    swipe(Location(552,530),Location(547,886))  --倒數第三格
    wait(0.4)
    swipe(Location(386,530),Location(367,886))
  end
  sleep(0.5)
  repeat
    join_team:existsClick("join_team.png",0)
    wait(0.5)
    swipe(Location(448,986),Location(396,986))
  until star2:exists("star2.png",0)
  exit_team:existsClick("agate_exit.png",0)
end

-- =使用者自訂=========
-- dialogInit()
-- addCheckBox('pvp_fight','pvp',false)  --是否打PVP
-- addCheckBox('feed_food','練肥',false)  --是否打練肥
-- addCheckBox('friend','朋友決鬥',false)  --是否打好友
-- dialogShowFullScreen("關卡設定")



-- while (true) do
-- 打PVP
-- if pvp_fight == true then
--   pvp()
-- end
--練肥
feed_food = true
if feed_food == true then
  food()
end
--打好友
-- if friend == true then
--   friend_PVP()
-- end
-- end