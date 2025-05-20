INSERT INTO activities (id, name, parent_id) VALUES
  (1, 'Еда',              NULL),
  (2, 'Мясная продукция', 1   ),
  (3, 'Молочная продукция',1   ),
  (4, 'Автомобили',        NULL),
  (5, 'Легковые',          4   ),
  (6, 'Запчасти',          4   );

INSERT INTO buildings (id, address, longitude, latitude) VALUES
  (1, 'ул. Ленина, 10',     37.6173, 55.7558),
  (2, 'пр. Московский, 45', 30.3141, 59.9386);

INSERT INTO organizations (id, tel, name, building_id) VALUES
  (1, '2-222-222', 'Рога и Копыта', 1),
  (2, '3-333-333', 'Молочная ферма', 1),
  (3, '4-444-444', 'ЗаборАвто',      2),
  (4, '5-555-555', 'ШинСервис',      2),
  (5, '6-666-666', 'АвтоМаркет',     2);

INSERT INTO organization_activity (organization_id, activity_id) VALUES
  (1, 2), 
  (1, 3), 
  (2, 3),  
  (3, 4),  
  (4, 5),  
  (5, 6);  
