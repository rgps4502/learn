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
pvpOver = Region(600, 236, 80, 45)
pvpNotirck = Region(696, 240, 62, 35)
function pvp()
    find_pvp:existsClick('find_pvp.png', 1)
    if pvp1:exists('pvp1.png', 1) then
        pvp1:existsClick('pvp1.png', 1)
        if pvpNotirck:exists('pvpNoTrick.png', 1.5) then
            click(Location(952, 201))
            sleep(300)
        elseif not pvp1:exists('pvp1.png', 1) then
            click(Location(1061, 514))
            if pvpAuto:exists('pvpAuto.png', 60) then
                click(Location(236, 675))
            end
            pvpOver:existsClick('pvpOver.png', 300)
        end
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
