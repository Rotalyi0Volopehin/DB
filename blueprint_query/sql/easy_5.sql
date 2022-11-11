SELECT DISTINCT courier_name, courier_surname, courier_ex, courier_telephone
FROM pizza_order RIGHT JOIn courier USING (courier_id)
WHERE courier_id not in (SELECT courier_id FROM pizza_order RIGHT JOIn courier USING (courier_id) WHERE order_status_deliver = "no");