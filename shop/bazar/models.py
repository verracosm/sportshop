from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):
	name = models.CharField(verbose_name='Product Categories', max_length = 50, unique = True)

	def __str__(self):
		return '{0}'.format(self.name)

# 				<SQL CODE>	
#-- Table: public.bazar_productcategory
#
#-- DROP TABLE public.bazar_productcategory;
#
#CREATE TABLE public.bazar_productcategory
#(
#    id integer NOT NULL DEFAULT nextval('bazar_productcategory_id_seq'::regclass),
#    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
#    CONSTRAINT bazar_productcategory_pkey PRIMARY KEY (id),
#    CONSTRAINT bazar_productcategory_name_key UNIQUE (name)
#
#)
#WITH (
#    OIDS = FALSE
#)
#TABLESPACE pg_default;
#
#ALTER TABLE public.bazar_productcategory
#    OWNER to postgres;
#
#-- Index: bazar_productcategory_name_1ecec98a_like
#
#-- DROP INDEX public.bazar_productcategory_name_1ecec98a_like;
#
#CREATE INDEX bazar_productcategory_name_1ecec98a_like
#    ON public.bazar_productcategory USING btree
#    (name COLLATE pg_catalog."default" varchar_pattern_ops)
#    TABLESPACE pg_default;	

class Product(models.Model):
	name 		= models.CharField(max_length = 50)
	description = models.TextField(max_length = 500)
	price		= models.FloatField(default = 0)
	amount		= models.IntegerField(default = 0)
	category    = models.ManyToManyField(ProductCategory)

	def __str__(self):
		return '{0}'.format(self.name)

# 				<SQL CODE>	
#-- Table: public.bazar_product
#
#-- DROP TABLE public.bazar_product;
#
#CREATE TABLE public.bazar_product
#(
#    id integer NOT NULL DEFAULT nextval('bazar_product_id_seq'::regclass),
#    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
#    description text COLLATE pg_catalog."default" NOT NULL,
#    price double precision NOT NULL,
#    amount integer NOT NULL,
#    CONSTRAINT bazar_product_pkey PRIMARY KEY (id)
#)
#WITH (
#    OIDS = FALSE
#)
#TABLESPACE pg_default;
#
#ALTER TABLE public.bazar_product
#    OWNER to postgres;


class Baskecior(models.Model):
	user 	= models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	amount 	= models.IntegerField(default=1)

	def __str__(self):
		return '{0} {1}'.format(self.user.id, self.product.id)

# 				<SQL CODE>	
#-- Table: public.bazar_baskecior
#
#-- DROP TABLE public.bazar_baskecior;
#
#CREATE TABLE public.bazar_baskecior
#(
#    id integer NOT NULL DEFAULT nextval('bazar_baskecior_id_seq'::regclass),
#    product_id integer NOT NULL,
#    user_id integer NOT NULL,
#    amount integer NOT NULL,
#    CONSTRAINT bazar_baskecior_pkey PRIMARY KEY (id),
#    CONSTRAINT bazar_baskecior_product_id_a3347a38_fk_bazar_product_id FOREIGN KEY (product_id)
#        REFERENCES public.bazar_product (id) MATCH SIMPLE
#        ON UPDATE NO ACTION
#        ON DELETE NO ACTION
#        DEFERRABLE INITIALLY DEFERRED,
#    CONSTRAINT bazar_baskecior_user_id_2958fd87_fk_auth_user_id FOREIGN KEY (user_id)
#        REFERENCES public.auth_user (id) MATCH SIMPLE
#        ON UPDATE NO ACTION
#        ON DELETE NO ACTION
#        DEFERRABLE INITIALLY DEFERRED
#)
#WITH (
#    OIDS = FALSE
#)
#TABLESPACE pg_default;
#
#ALTER TABLE public.bazar_baskecior
#    OWNER to postgres;
#
#-- Index: bazar_baskecior_product_id_a3347a38
#
#-- DROP INDEX public.bazar_baskecior_product_id_a3347a38;
#
#CREATE INDEX bazar_baskecior_product_id_a3347a38
#    ON public.bazar_baskecior USING btree
#    (product_id)
#    TABLESPACE pg_default;
#
#-- Index: bazar_baskecior_user_id_2958fd87
#
#-- DROP INDEX public.bazar_baskecior_user_id_2958fd87;
#
#CREATE INDEX bazar_baskecior_user_id_2958fd87
#    ON public.bazar_baskecior USING btree
#    (user_id)
#    TABLESPACE pg_default;

class Order(models.Model):
	user 	= models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	amount 	= models.IntegerField(default=0)

	class OrderStatus:
		UNPAID = 1
		PAID   = 2

		CHOICES = (
			(PAID, 'PAID'),
			(UNPAID, 'UNPAID')
		)

	order_status = models.IntegerField(choices=OrderStatus.CHOICES, default=OrderStatus.UNPAID)

def __str__(self):
		return '{0} {1}'.format(self.user.id, self.product.id)

# 				<SQL CODE>	
#		-- Table: public.bazar_order
#
#-- DROP TABLE public.bazar_order;
#
#CREATE TABLE public.bazar_order
#(
#    id integer NOT NULL DEFAULT nextval('bazar_order_id_seq'::regclass),
#    product_id integer NOT NULL,
#    user_id integer NOT NULL,
#    amount integer NOT NULL,
#    order_status integer NOT NULL,
#    CONSTRAINT bazar_order_pkey PRIMARY KEY (id),
#    CONSTRAINT bazar_order_product_id_93983ba2_fk_bazar_product_id FOREIGN KEY (product_id)
#        REFERENCES public.bazar_product (id) MATCH SIMPLE
#        ON UPDATE NO ACTION
#        ON DELETE NO ACTION
#        DEFERRABLE INITIALLY DEFERRED,
#    CONSTRAINT bazar_order_user_id_79d483b4_fk_auth_user_id FOREIGN KEY (user_id)
#        REFERENCES public.auth_user (id) MATCH SIMPLE
#        ON UPDATE NO ACTION
#        ON DELETE NO ACTION
#        DEFERRABLE INITIALLY DEFERRED
#)
#WITH (
#    OIDS = FALSE
#)
#TABLESPACE pg_default;
#
#ALTER TABLE public.bazar_order
#    OWNER to postgres;
#
#-- Index: bazar_order_product_id_93983ba2
#
#-- DROP INDEX public.bazar_order_product_id_93983ba2;
#
#CREATE INDEX bazar_order_product_id_93983ba2
#    ON public.bazar_order USING btree
#    (product_id)
#    TABLESPACE pg_default;
#
#-- Index: bazar_order_user_id_79d483b4

#-- DROP INDEX public.bazar_order_user_id_79d483b4;
#
#CREATE INDEX bazar_order_user_id_79d483b4
#    ON public.bazar_order USING btree
#    (user_id)
#    TABLESPACE pg_default;