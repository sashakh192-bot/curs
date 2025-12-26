# Набор аналитических запросов (без SQL-файлов — только выполнение).
# Таблицы ожидаются такие: users, scooters, tariffs, zones, trips, payments, fines.

QUERIES = [
    (
        "1. Доступные электросамокаты (топ-10 по заряду)",
        """
        SELECT scooter_id, model, status, battery_pct
        FROM scooters
        WHERE status = 'available'
        ORDER BY battery_pct DESC
        LIMIT 10;
        """
    ),
    (
        "2. Самокаты на обслуживании",
        """
        SELECT scooter_id, model, battery_pct
        FROM scooters
        WHERE status = 'service'
        ORDER BY battery_pct ASC;
        """
    ),
    (
        "3. Тарифы аренды",
        """
        SELECT tariff_id, tariff_name, unlock_fee, price_per_min
        FROM tariffs
        ORDER BY tariff_id;
        """
    ),
    (
        "4. Зоны парковки",
        """
        SELECT zone_id, zone_name, zone_type
        FROM zones
        ORDER BY zone_id;
        """
    ),
    (
        "5. Топ-5 поездок по стоимости",
        """
        SELECT t.trip_id, u.full_name, t.total_min, t.total_cost
        FROM trips t
        JOIN users u ON u.user_id = t.user_id
        ORDER BY t.total_cost DESC
        LIMIT 5;
        """
    ),
    (
        "6. Выручка по успешным платежам",
        """
        SELECT COALESCE(SUM(amount), 0) AS revenue_paid
        FROM payments
        WHERE pay_status = 'paid';
        """
    ),
    (
        "7. Средняя длительность поездки (мин)",
        """
        SELECT ROUND(AVG(total_min)::numeric, 2) AS avg_minutes
        FROM trips;
        """
    ),
    (
        "8. Популярные зоны завершения поездок",
        """
        SELECT z.zone_name, COUNT(*) AS trips_count
        FROM trips t
        LEFT JOIN zones z ON z.zone_id = t.end_zone_id
        GROUP BY z.zone_name
        ORDER BY trips_count DESC;
        """
    ),
    (
        "9. Штрафы (список)",
        """
        SELECT f.fine_id, f.fine_type, f.fine_amount, f.created_at, f.trip_id
        FROM fines f
        ORDER BY f.fine_id;
        """
    ),
    (
        "10. Статусы самокатов (сколько в каждом состоянии)",
        """
        SELECT status, COUNT(*) AS cnt
        FROM scooters
        GROUP BY status
        ORDER BY cnt DESC;
        """
    ),
]
