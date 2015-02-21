import System.Environment

main = do
    args <- getArgs
    print ("Hello, world!" ++ unwords args ++ "END")
