        self.cursor.execute (
            '''CREATE TABLE IF NOT EXISTS User (
            user_id INT NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(45) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(45) NOT NULL,
            profile_image VARCHAR(255) DEFAULT NULL,
            password VARCHAR(45) NOT NULL,
            birthdate DATE NOT NULL,
            country VARCHAR(45) DEFAULT NULL,
            accepted_terms TINYINT NOT NULL DEFAULT '0',
            PRIMARY KEY (user_id),
            UNIQUE KEY email_UNIQUE (email)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci '''
        )
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)