-- we create  a trigger after we update something
-- always trigger
DELIMITER $$

CREATE TRIGGER decrease AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END$$

DELIMITER ;
