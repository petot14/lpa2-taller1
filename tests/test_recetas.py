from recetas.recetas import calcular_ingredientes

def test_01():
  assert calcular_ingredientes(0) == (0.0, 0.0, 0.0, 0.0)

def test_02():
  assert calcular_ingredientes(4) == (225.0, 1.0, 100.0, 200.0)

def test_03():
  assert calcular_ingredientes(8) == (450.0, 2.0, 200.0, 400.0)

def test_04():
  assert calcular_ingredientes(12) == (675.0, 3.0, 300.0, 600.0)

def test_05():
  assert calcular_ingredientes(1) == (0.0, 0.0, 0.0, 0.0)

def test_06():
  assert calcular_ingredientes(3) == (0.0, 0.0, 0.0, 0.0)

def test_07():
  assert calcular_ingredientes(-1) == (0.0, 0.0, 0.0, 0.0)

def test_08():
  assert calcular_ingredientes(-4) == (0.0, 0.0, 0.0, 0.0)
