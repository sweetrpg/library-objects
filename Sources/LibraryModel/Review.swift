//
// Review.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class Review : Model {
    public static let schema = Review.v20210625.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Review.v20210625.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Review.v20210625.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: Review.v20210625.title)
    public var title : String

    @Field(key: Review.v20210625.text)
    public var text : String

    @Parent(key: Review.v20210625.volumeId)
    public var volume : Volume

    @Timestamp(key: Review.v20210625.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, title : String, volumeId : Volume.IDValue) {
        self.id = id
        self.title = title
        self.$volume.id = volumeId
    }

}

extension Review : Content {}
