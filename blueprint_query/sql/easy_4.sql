SELECT courier_name, courier_surname, courier_ex, courier_telephone, order_date_create, order_time_depart, order_summary_price, order_meals_amount
FROM pizza_order JOIN courier USING (courier_id)  WHERE order_status_deliver = "no"