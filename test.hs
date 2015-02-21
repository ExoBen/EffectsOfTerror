import System.Environment
import System.IO

main = do
    contents <- hGetContents stdin
    print ("Hello, world!" ++ contents ++ "END")
