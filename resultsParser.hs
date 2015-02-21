-- INTRODUCTION ---------------------------------------------------------------
--
--   Author:
--       Dr-Lord
--   Version:
--       0.1 - 21/02/2015
--
--   Repository:
--       https://github.com/ExogenesisBen/EffectsOfTerror
--
--   Description:
--      This program is meant to take Global Terrorism Database grep search
--      results and return specific fields from them.
--
--   Sections:
--       1 - Imports and Type declarations
--       2 - Main Functions
--       3 - Other Functions
--       4 - Data

---- 1 - IMPORTS AND TYPE DECLARATIONS -----------------------------------------

import System.Environment
import System.IO
import qualified Data.Map as M


---- 2 - MAIN FUNCTIONS --------------------------------------------------------

main = do
    --contents <- hGetContents stdin
    handle <- openFile "testSearch.txt" ReadMode
    hSetEncoding handle utf8
    contents <- hGetContents handle

    let results = map (splitOn '¬') $ lines contents

--    print contents
--    print . length $ results!!0
    print $ extract (priInds,secInds) results



---- 3 - OTHER FUNCTIONS -------------------------------------------------------

    -- Extract primary and secondary fields from row lists
extract :: ([Int],[Int]) -> [[String]] -> [[[String]]]
extract (pri, sec) results = map func results
    where func row = [priVals row, secVals row]

          priVals row = map (row!!) priInds
          secVals row = map (row!!) secInds


--    where func :: [String] -> [[String]]
--          func row = (\x-> [fst x, snd x]) . fst $ foldr step (([],[]),133) row
--
--          step :: String -> (([String],[String]),Int) -> (([String],[String]),Int)
--          step val (fs@(f,s),i)
--            | i `elem` pri = ((val:f,s),i-1)
--            | i `elem` sec = ((f,val:s),i-1)
--            | otherwise    = (fs,       i-1)


    -- Basic split function at predicate of current char
splitOn :: Char -> String -> [String]
splitOn c str = m:ms
    where (ms,m) = foldr step ([],[]) str
          step :: Char -> ([String],String) -> ([String],String)
          step x (a,b)
            | x /= c    = (a,x:b)
            | otherwise = (b:a,[])


    -- Generate a reverse lookup map between column titles and their indexes
generateLookupMap :: [String] -> M.Map String Int
generateLookupMap strs = M.fromList $ zip strs [0..(length strs)-1]


    -- Extract indexes from field names
index :: String -> Int
index field = case M.lookup field titles of
        Just x  -> x
        Nothing -> 0



---- 4 - DATA ------------------------------------------------------------------

priInds = map index primary
secInds = map index secondary

primary   = splitOn ',' "iyear,imonth,iday,location,city,region_txt,provstate,country_txt"
secondary = splitOn ',' "summary,nkill,nwound,propvalue,attacktype1_txt,target1,targtype1_txt,weaptype1_txt"

    -- M.size titles == 134
titles = generateLookupMap titleList

titleList = splitOn ',' "eventid,iyear,imonth,iday,approxdate,extended,resolution,country,country_txt,region,region_txt,provstate,city,latitude,longitude,specificity,vicinity,location,summary,crit1,crit2,crit3,doubtterr,alternative,alternative_txt,multiple,success,suicide,attacktype1,attacktype1_txt,attacktype2,attacktype2_txt,attacktype3,attacktype3_txt,targtype1,targtype1_txt,targsubtype1,targsubtype1_txt,corp1,target1,natlty1,natlty1_txt,targtype2,targtype2_txt,targsubtype2,targsubtype2_txt,corp2,target2,natlty2,natlty2_txt,targtype3,targtype3_txt,targsubtype3,targsubtype3_txt,corp3,target3,natlty3,natlty3_txt,gname,gsubname,gname2,gsubname2,gname3,gsubname3,motive,guncertain1,guncertain2,guncertain3,nperps,nperpcap,claimed,claimmode,claimmode_txt,claim2,claimmode2,claimmode2_txt,claim3,claimmode3,claimmode3_txt,compclaim,weaptype1,weaptype1_txt,weapsubtype1,weapsubtype1_txt,weaptype2,weaptype2_txt,weapsubtype2,weapsubtype2_txt,weaptype3,weaptype3_txt,weapsubtype3,weapsubtype3_txt,weaptype4,weaptype4_txt,weapsubtype4,weapsubtype4_txt,weapdetail,nkill,nkillus,nkillter,nwound,nwoundus,nwoundte,property,propextent,propextent_txt,propvalue,propcomment,ishostkid,nhostkid,nhostkidus,nhours,ndays,divert,kidhijcountry,ransom,ransomamt,ransomamtus,ransompaid,ransompaidus,ransomnote,hostkidoutcome,hostkidoutcome_txt,nreleased,addnotes,scite1,scite2,scite3,dbsource,INT_LOG,INT_IDEO,INT_MISC,INT_ANY,related"
