-- Agregar un nuevo producto al inventario
addProduct :: [(String, Double, Int)] -> String -> Double -> Int -> [(String, Double, Int)]
addProduct inventory name price quantity = inventory ++ [(name, price, quantity)]

-- Actualizar la cantidad de un producto existente
updateQuantity :: [(String, Double, Int)] -> String -> Int -> [(String, Double, Int)]
updateQuantity [] _ _ = []
updateQuantity ((n, p, q):xs) name newQuantity
    | n == name = (n, p, newQuantity) : xs
    | otherwise = (n, p, q) : updateQuantity xs name newQuantity

-- Eliminar un producto del inventario
removeProduct :: [(String, Double, Int)] -> String -> [(String, Double, Int)]
removeProduct inventory name = filter (\(n, _, _) -> n /= name) inventory

-- Resumen del inventario: total de productos y valor total
inventorySummary :: [(String, Double, Int)] -> (Int, Double)
inventorySummary inventory = (totalQuantity, totalValue)
  where
    totalQuantity = sum [q | (_, _, q) <- inventory]
    totalValue = sum [p * fromIntegral q | (_, p, q) <- inventory]

-- Busca un producto por su nombre y devuelve su precio y cantidad en stock
searchProduct :: [(String, Double, Int)] -> String -> Maybe (Double, Int)
searchProduct [] _ = Nothing
searchProduct ((n, p, q) : xs) name
    | n == name = Just(p, q)
    | otherwise = searchProduct xs name

-- Aplica un descuento a todos los productos del inventario
applyDiscount :: [(String, Double, Int)] -> Double -> [(String, Double, Int)]
applyDiscount inventory discount =
    [(n, p * (1 - discount / 100), q) | (n, p, q) <- inventory]

main :: IO()
main = do
    let inventory = []
    let inventory1 = addProduct inventory "Manzanas" 0.5 100
    let inventory2 = addProduct inventory1 "Platanos" 0.3 150
    let inventory3 = updateQuantity inventory2 "Manzanas" 120
    let inventory4 = removeProduct inventory3 "Platanos"
    let (totalQty, totalValue) = inventorySummary inventory4
    
    putStrLn $ "Inventario Final: " ++ show inventory4
    putStrLn $ "Total de productos en stock: " ++ show totalQty
    putStrLn $ "Valor total del inventario: " ++ show totalValue

    case searchProduct inventory4 "Manzanas" of
        Just(value, qty) -> putStrLn $ "Precio: " ++ show value ++ ", Cantidad: " ++ show qty
        Nothing -> putStrLn "No existe un producto con ese nombre."

    let inventory5 = applyDiscount inventory4 20
    putStrLn $ "Inventario con 20% de descuento aplicado: " ++ show inventory5
