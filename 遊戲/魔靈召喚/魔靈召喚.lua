-- ========== Settings ================
Settings:setCompareDimension(true, 1280) --模擬器寬
Settings:setScriptDimension(true, 1280)
Settings:set('MinSimilarity', 0.8) --圖片精準度

-- =========區域=======
-- Region:highlight() -- 讓紅色框框出現 ex: night:highlight() 再調用一次消失
--PVP----------------------------
find_pvp = Region(237, 212, 304, 275)
pvp1 = Region(977, 153, 92, 462)
pvpAuto = Region(1175, 52, 100, 100)
pvpAuto2 = Region(206, 645, 58, 54)
pvpOver = Region(600, 236, 80, 45)
pvpOver2 = Region(592, 159, 60, 29)
pvpNotirck = Region(696, 240, 62, 35)
network_err = Region(468, 256, 98, 38)
network_err2 = Region(491, 281, 88, 35)
reflush = Region(930, 159, 53, 27)
-- 網路斷線
function network()
    if network_err:exists('network_err.png', 0) then
        click(Location(521, 437))
    end
    if network_err2:exists('network_err2.png', 0) then
        click(Location(637, 434))
    end
end

function swip_down()
    p1 = Location(850, 614)
    p2 = Location(850, 188)

    setManualTouchParameter(50, 1) -- 詳見下面解說

    actionList = {
        {action = 'touchDown', target = p1},
        {action = 'wait', target = 0.2},
        {action = 'touchMove', target = p2},
        {action = 'touchUp', target = p2}
    }

    manualTouch(actionList)
end

function pvp()
    find_pvp:existsClick('find_pvp.png', 1)
    if pvp1:exists('pvp1.png', 1) then
        pvp1:existsClick('pvp1.png', 1)
        if pvpNotirck:exists('pvpNoTrick.png', 1) then
            click(Location(952, 201))
            sleep(600)
            reflush:existsClick('reflush.png', 0)
        elseif not pvp1:exists('pvp1.png', 0) then
            click(Location(1061, 514))
            if pvpAuto2:exists('pvpAuto2.png', 600) then
                sleep(1)
                click(Location(236, 675))
            end
            -- 等待戰鬥結束
            repeat
                sleep(3)
            until pvpOver:existsClick('pvpOver.png', 0)
            sleep(1)
            pvpOver2:existsClick('pvpOver2.png', 0)
        end
    else
        swip_down()
    end
end

while (true) do
    pvp()
end
-- 找圖+xy方法
-- match = pvp1:find('pvp1.png')
-- x = match.x + 138
-- y = match.y
-- click(Location(x, y))
