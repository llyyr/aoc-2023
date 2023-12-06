solve :: (Double, Double) -> Int
solve (t, d) = let
    root = sqrt (t^2 - 4*d)
    hi = (t + root) / 2
    lo = (t - root) / 2
    in ceiling hi - floor lo - 1

parse :: String -> ([String] -> [String]) -> [(Double, Double)]
parse content transform = let
    l = lines content
    times = map read $ transform $ tail $ words (l !! 0)
    distances = map read $ transform $ tail $ words (l !! 1)
    in zip times distances

main :: IO ()
main = do
    inp <- readFile "06.txt"
    putStrLn $ "Part 1: " ++ show (product $ map solve $ parse inp id)
    putStrLn $ "Part 2: " ++ show (product $ map solve $ parse inp (pure . concat))
